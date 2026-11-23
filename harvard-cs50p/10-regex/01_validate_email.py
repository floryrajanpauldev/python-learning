
import re

email = input("Enter your email: ")

pattern = r"^[a-zA-Z0-9_]+([.-][a-zA-Z0-9_]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.[a-zA-Z]{2,}$"

pattern2 = r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"

if re.search(pattern2, email, re.IGNORECASE):
    print("Valid email")
else:
    print("Invalid email")


"""
Examples
Email	Result
john@gmail.com	Valid
john.doe@gmail.com	Valid
john_123@yahoo.com	Valid
john-smith@example.edu	Valid
john@example.co.uk	Valid
john@gmail	Invalid
john@.com	Invalid
john@@gmail.com	Invalid
@gmail.com	Invalid


"""