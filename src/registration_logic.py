import asyncio
import random
from faker import Faker
import bcrypt
from loguru import logger
from utils import read_proxies_from_file, write_data_to_file, format_log_message, validate_email
from account_manager import AccountManager
from email_handler import EmailHandler
from proxy_manager import ProxyManager
import requests
from bs4 import BeautifulSoup
import re

async def register_account(num_accounts, referral_code):
    fake = Faker()
    account_manager = AccountManager()
    email_handler = EmailHandler()
    proxy_manager = ProxyManager(read_proxies_from_file())

    successful_registrations = 0
    failed_registrations = 0
    
    for _ in range(num_accounts):
        try:
            proxy = proxy_manager.get_proxy()
            email = email_handler.get_email_address()
            password = fake.password(length=12, special_chars=True)
            username = fake.user_name()

            account_data = {
                "username": username,
                "password": bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                "email": email
            }

            registration_successful = await register_new_account(account_data, proxy, referral_code)
            if registration_successful:
                account_manager.save_account(account_data)
                logger.info(format_log_message("success", f"Account created successfully: {username}"))
                successful_registrations += 1
            else:
                logger.error(format_log_message("error", f"Account creation failed: {username}"))
                failed_registrations += 1
        
        except Exception as e:
            logger.exception(format_log_message("error", f"An unexpected error occurred: {e}"))
            failed_registrations += 1

    return successful_registrations, failed_registrations


async def register_new_account(account_data, proxy, referral_code):
    session = requests.Session()
    session.proxies = {"http": proxy, "https": proxy}

    try:
        # Simulate registration process (replace with actual website interaction)
        response = session.post("https://app.nodepay.ai/register", data=account_data, timeout=30)
        response.raise_for_status()

        # Check for success, handle redirects and verification if needed
        soup = BeautifulSoup(response.content, 'html.parser')
        success_message = soup.find(id="success_message")
        if success_message:
            return True
        else:
            error_message = soup.find(id="error_message")
            if error_message:
              logger.error(f"Registration error: {error_message.text}")
            return False
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error during registration: {e}")
        return False
    except Exception as e:
        logger.exception(f"An unexpected error occurred during registration: {e}")
        return False


```