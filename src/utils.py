import os
import json
import re
from loguru import logger

def read_proxies_from_file(filepath="data/proxies.txt"):
    """Reads proxy servers from a file.

    Args:
        filepath: Path to the proxy file.

    Returns:
        A list of proxy servers, or None if the file is not found or empty.  Each element is a string.
    """
    try:
        with open(filepath, "r") as f:
            proxies = [line.strip() for line in f if line.strip()]
        return proxies if proxies else None
    except FileNotFoundError:
        logger.error(f"Proxy file not found: {filepath}")
        return None
    except Exception as e:
        logger.exception(f"Error reading proxy file: {e}")
        return None

def write_data_to_file(filepath, data, mode="w"):
    """Writes data to a file.

    Args:
        filepath: Path to the file.
        data: Data to write.  Should be JSON serializable.
        mode: File opening mode ("w" for write, "a" for append).
    """
    try:
        with open(filepath, mode, encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except (FileNotFoundError, IOError, OSError) as e:
        logger.exception(f"Error writing to file {filepath}: {e}")
    except Exception as e:
        logger.exception(f"An unexpected error occurred: {e}")


def validate_email(email):
    """Validates email format using regular expression."""
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def format_log_message(level, message, details=None):
    """Formats log messages for better readability."""
    formatted_message = f"[{level.upper()}] {message}"
    if details:
        formatted_message += f": {details}"
    return formatted_message


def get_config(filepath="config/config.yaml"):
    """Reads configuration from a YAML file."""
    try:
        with open(filepath, 'r') as file:
            return yaml.safe_load(file)
    except FileNotFoundError:
        logger.error(f"Config file not found: {filepath}")
        return {}
    except yaml.YAMLError as e:
        logger.error(f"Error parsing YAML config: {e}")
        return {}
    except Exception as e:
        logger.exception(f"An unexpected error occurred while reading config file: {e}")
        return {}

def generate_random_string(length=10):
    import random
    import string
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def check_file_exists(filepath):
    return os.path.exists(filepath)

def create_directory_if_not_exists(path):
    os.makedirs(path, exist_ok=True)

```