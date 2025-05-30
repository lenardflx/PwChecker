# Password Security Checker

A Python-based CLI tool to check the security of a password. The tool checks whether a password has been pwned (compromised in data breaches), identifies common weak passwords, and provides recommendations on how to improve the password's security.

## Features

- **Pwned Password Check**: Uses the HaveIBeenPwned API to check if a password has been compromised.
- **Common Password Detection**: Checks if the password is a commonly used weak password using a local comparison file.
- **Security Recommendations**: Provides feedback based on password length, complexity, and structure.

## Project Structure

```
pwchecker/
├── pwchecker.py         # Main Python script
├── common_passwords.txt # Common passwords Text File for Comparison
├── setup.py             # Setup file for installing the CLI tool
├── README.md            # This file
└── requirements.txt     # Required libraries for this project

```

## Prerequisites

- **Python 3.x**: Make sure Python 3.x is installed on your system.
- **Required Libraries**: Install the libraries listed in the `requirements.txt` file.

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/pwchecker.git
   cd pwchecker
   ```

2. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Usage

### CLI

To use the password checker via the command line, you can either pass the password as an argument or enter it when prompted.

1. **Pass the password as a command-line argument**:
   ```
   pwchecker "your_password"
   ```

2. **Without an argument (you'll be prompted to enter the password)**:
   ```
   pwchecker
   ```

### Sample Output

The output will include:

- A **Pwned Password Warning** if the password has been found in known data breaches.
- A **Common Password Warning** if the password matches any commonly used passwords.
- **Security Recommendations** if the password does not meet recommended security standards.

Example:
```
⚠️ WARNING: This password does not meet the recommended security standards:
⚠️ WARNING: - Password should be at least 12 characters long.
⚠️ WARNING: - Password should contain at least one special character.
---
Good news: This password has not been found in any known data breaches.
```

## Security and Privacy

The tool is designed to prioritize user privacy and security:
- **Client-Side Hashing**: Passwords are hashed locally before querying the HaveIBeenPwned API. Only the first 5 characters of the SHA-1 hash are sent to the API, ensuring that the original password is never exposed.
- **Local Password Comparison**: Common password checks are performed locally using `common_passwords.txt`, so no data is sent externally.

## License

This project is licensed under the MIT License.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue if you would like to contribute.

---

**Disclaimer**: This tool is for educational and personal use only. Always follow security best practices when handling passwords, and never share sensitive information.