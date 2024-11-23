import argparse
import asyncio
from registration_logic import register_account
from utils import format_log_message
from loguru import logger

async def main():
    parser = argparse.ArgumentParser(description="NodePay.ai Automated Registration Bot")
    parser.add_argument("-n", "--num_accounts", type=int, required=True, help="Number of accounts to create")
    parser.add_argument("-r", "--referral_code", type=str, help="Referral code (optional)")
    args = parser.parse_args()

    logger.info(format_log_message("info", "Starting registration process..."))
    try:
        successful_registrations, failed_registrations = await register_account(args.num_accounts, args.referral_code)
        logger.info(format_log_message("success", f"Registration complete. Successful: {successful_registrations}, Failed: {failed_registrations}"))

    except Exception as e:
        logger.exception(format_log_message("error", f"An unexpected error occurred: {e}"))


if __name__ == "__main__":
    asyncio.run(main())

```