import asyncio
import re
from bs4 import BeautifulSoup
import requests
from loguru import logger
from utils import format_log_message, get_config

class EmailHandler:
    def __init__(self):
        self.config = get_config()
        self.email_provider = self.config.get("email_provider", "tempmail")  # Default to tempmail
        self.email_api_url = self.config.get(f"{self.email_provider}_api_url")
        self.email_address = None


    def get_email_address(self):
        try:
            if self.email_api_url:
                response = requests.get(self.email_api_url)
                response.raise_for_status()
                email = response.json().get("email")
                if email:
                    self.email_address = email
                    return email
                else:
                    logger.error(format_log_message("error", f"Failed to get email address from {self.email_provider} API"))
                    return None
            else:
                logger.error(format_log_message("error", "Email API URL not configured"))
                return None

        except requests.exceptions.RequestException as e:
            logger.exception(format_log_message("error", f"Error connecting to {self.email_provider} API: {e}"))
            return None
        except (KeyError, ValueError) as e:
            logger.exception(format_log_message("error", f"Error parsing {self.email_provider} API response: {e}"))
            return None
        except Exception as e:
            logger.exception(format_log_message("error", f"An unexpected error occurred: {e}"))
            return None

    def get_verification_code(self, email_address):
      try:
        if self.email_api_url:
          inbox_url = f"{self.email_api_url}/inbox"
          response = requests.get(inbox_url)
          response.raise_for_status()
          emails = response.json().get("emails", [])
          for email in emails:
              if email_address in email["from"]:
                  body = email.get("body", "")
                  match = re.search(r"([0-9]{6})", body)
                  if match:
                    return match.group(1)

          return None
        else:
          logger.error(format_log_message("error", "Email API URL not configured"))
          return None

      except requests.exceptions.RequestException as e:
          logger.exception(format_log_message("error", f"Error connecting to {self.email_provider} API: {e}"))
          return None
      except (KeyError, ValueError, TypeError) as e:
          logger.exception(format_log_message("error", f"Error parsing {self.email_provider} API response: {e}"))
          return None
      except Exception as e:
          logger.exception(format_log_message("error", f"An unexpected error occurred: {e}"))
          return None

    def check_email(self, email_address, timeout=30):
      try:
        if not self.email_address:
          return False

        for _ in range(timeout):
          code = self.get_verification_code(email_address)
          if code:
            return code
          asyncio.sleep(1)

        return None
      except Exception as e:
          logger.exception(format_log_message("error", f"An unexpected error occurred during email check: {e}"))
          return None

```