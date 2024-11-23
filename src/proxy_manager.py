import random
import socks
import socket
from loguru import logger
from PySocks import ProxyError, GeneralProxyError
from utils import read_proxies_from_file, format_log_message

class ProxyManager:
    def __init__(self, proxies):
        self.proxies = proxies
        self.current_proxy = None

    def get_proxy(self):
        if not self.proxies:
            logger.error(format_log_message("error", "No proxies available."))
            return None
        if self.current_proxy and self.is_proxy_working(self.current_proxy):
            return self.current_proxy
        self.current_proxy = random.choice(self.proxies)
        return self.current_proxy

    def rotate_proxy(self):
        if self.proxies:
            self.current_proxy = random.choice(self.proxies)

    def is_proxy_working(self, proxy):
        try:
            sock = socks.socksocket()
            proxy_type, proxy_address = proxy.split("://")
            proxy_host, proxy_port = proxy_address.split(":")
            proxy_port = int(proxy_port)
            if proxy_type == "http":
                sock.set_proxy(socks.HTTP, proxy_host, proxy_port)
            elif proxy_type == "socks4":
                sock.set_proxy(socks.SOCKS4, proxy_host, proxy_port)
            elif proxy_type == "socks5":
                sock.set_proxy(socks.SOCKS5, proxy_host, proxy_port)
            else:
                logger.error(format_log_message("error", f"Unsupported proxy protocol: {proxy_type}"))
                return False
            sock.connect(("google.com", 80))
            sock.close()
            return True
        except (ProxyError, GeneralProxyError, socket.error, OSError) as e:
            logger.warning(format_log_message("warning", f"Proxy {proxy} is not working: {e}"))
            return False
        except Exception as e:
            logger.exception(format_log_message("error", f"An unexpected error occurred while checking proxy: {e}"))
            return False

```