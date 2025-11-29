import re

data = """
Mobile: 9876543210
PAN: ABCDE1234F
Aadhaar: 123412341234
PIN: 560001
URL: https://www.google.com
IP: 192.168.1.1
Password: Abc@1234
"""

# Regex patterns
patterns = {
    "Indian Mobile No": r"\b[6-9]\d{9}\b",
    "PAN Card": r"\b[A-Z]{5}[0-9]{4}[A-Z]\b",
    "Aadhaar": r"\b\d{12}\b",
    "Postal PIN": r"\b[1-9][0-9]{5}\b",
    "URL": r"https?://[A-Za-z0-9./_-]+",
    "IPv4": r"\b(?:\d{1,3}\.){3}\d{1,3}\b",
    "Strong Password": r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&+=]).{8,}$",
}

# Extraction
for name, pattern in patterns.items():
    match = re.findall(pattern, data)
    print(f"{name}: {match}")
