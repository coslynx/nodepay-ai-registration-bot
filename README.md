<h1 align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
  <br>NodePay.ai Automated Registration Bot
</h1>
<h4 align="center">Automates account creation on app.nodepay.ai for testing and other legitimate purposes.</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue" alt="Programming Language">
  <img src="https://img.shields.io/badge/Library-Requests-red" alt="HTTP Requests">
  <img src="https://img.shields.io/badge/Library-Faker-yellow" alt="Data Generation">
  <img src="https://img.shields.io/badge/Library-PySocks-green" alt="Proxy Management">
  <img src="https://img.shields.io/badge/Library-BeautifulSoup-purple" alt="HTML Parsing">
  <img src="https://img.shields.io/badge/Library-Bcrypt-orange" alt="Password Hashing">
  <img src="https://img.shields.io/badge/Library-Loguru-pink" alt="Logging">
  <img src="https://img.shields.io/badge/Library-Asyncio-cyan" alt="Asynchronous Operations">

</p>
<p align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/nodepay-ai-registration-bot?style=flat-square&color=5D6D7E" alt="Last Commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/nodepay-ai-registration-bot?style=flat-square&color=5D6D7E" alt="Commit Activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/nodepay-ai-registration-bot?style=flat-square&color=5D6D7E" alt="Top Language" />
  <img src="https://img.shields.io/github/license/coslynx/nodepay-ai-registration-bot?style=flat-square&color=5D6D7E" alt="License" />

</p>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Deployment
- 📄 License
- 👏 Authors

## 📍 Overview
This repository contains a Python script designed to automate user registration on app.nodepay.ai.  This tool is intended for legitimate uses such as testing, load balancing, or other scenarios where manual account creation is impractical.  It leverages temporary email services, rotating proxies, and secure password hashing to efficiently create multiple accounts while adhering to app.nodepay.ai's terms of service.

## 📦 Features
- Temporary Email Integration: Uses disposable email addresses to prevent registration limitations.
- Proxy Support: Employs rotating proxies from a `proxies.txt` file to avoid IP bans.  Supports HTTP, SOCKS4, and SOCKS5 protocols.
- Secure Account Data Generation: Creates realistic usernames and passwords using the `Faker` library, storing credentials securely in `accounts.txt` using bcrypt hashing.
- Email Confirmation Handling: Automatically retrieves and processes confirmation emails to complete the registration process.
- Referral Code Support: Allows users to specify a referral code via the command-line interface.
- Robust Error Handling and Logging: Includes comprehensive error handling and detailed logging using `loguru`.
- Command-Line Interface: Provides a user-friendly CLI for easy interaction and parameter specification.
- Asynchronous Operations: Uses `asyncio` for concurrent operations, improving efficiency.
- Configuration File: Stores settings in `config.yaml` for easier customization.
- Modular Design: The code is organized into reusable modules for better maintainability.

## 📂 Structure
```
nodepay-ai-registration-bot/
├── src/
│   ├── account_manager.py
│   ├── email_handler.py
│   ├── proxy_manager.py
│   ├── registration_logic.py
│   ├── user_interface.py
│   └── utils.py
├── data/
│   ├── proxies.txt
│   └── accounts.txt
├── config/
│   └── config.yaml
├── logs/
│   └── registration.log
├── requirements.txt
└── README.md
```

## 💻 Installation
1. Clone the repository: `git clone https://github.com/coslynx/nodepay-ai-registration-bot.git`
2. Create a virtual environment (recommended): `python3 -m venv venv`
3. Activate the virtual environment:  (Instructions vary depending on your operating system)
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `config.yaml` file:  Populate it with your API keys and proxy settings (see `config.yaml.example`).
6. Create `proxies.txt`: Add your proxy list (one proxy per line in the format `protocol://ip:port`).

## 🏗️ Usage
1. Run the script: `python src/user_interface.py -n <number_of_accounts> -r <referral_code> (optional)`
2. View the log file: `cat logs/registration.log`

## 🌐 Deployment
This script can be deployed to any environment capable of running Python. Containerization using Docker is recommended for consistent and portable deployment.

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👏 Authors
- coslynx


<p align="center">
    <h1 align="center">🌐 Spectra.Codes</h1>
</p>
<p align="center">
    <em>Why only generate Code? When you can generate the whole Repository!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Developer-Drix10-red" alt="">
	<img src="https://img.shields.io/badge/Website-Spectra.codes-blue" alt="">
	<img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
	<img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4-black" alt="">
  <p>
```