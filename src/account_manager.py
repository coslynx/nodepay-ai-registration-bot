import bcrypt
import json
import os
from loguru import logger
from utils import write_data_to_file, format_log_message

class AccountManager:
    def __init__(self, accounts_filepath="data/accounts.txt"):
        self.accounts_filepath = accounts_filepath
        self.accounts = self.load_accounts()

    def load_accounts(self):
        try:
            with open(self.accounts_filepath, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            logger.warning(format_log_message("warning", f"Accounts file not found or invalid: {self.accounts_filepath}. Starting with an empty account list."))
            return []
        except Exception as e:
            logger.exception(format_log_message("error", f"An unexpected error occurred while loading accounts: {e}"))
            return []

    def save_account(self, account_data):
        try:
            self.accounts.append(account_data)
            with open(self.accounts_filepath, "w") as f:
                json.dump(self.accounts, f, indent=4)
            return True

        except Exception as e:
            logger.exception(format_log_message("error", f"An unexpected error occurred while saving account: {e}"))
            return False

    def get_account(self, username):
        for account in self.accounts:
            if account["username"] == username:
                return account
        return None

    def delete_account(self, username):
        self.accounts = [account for account in self.accounts if account["username"] != username]
        try:
            with open(self.accounts_filepath, "w") as f:
                json.dump(self.accounts, f, indent=4)
            return True
        except Exception as e:
            logger.exception(format_log_message("error", f"An unexpected error occurred while deleting account: {e}"))
            return False

```