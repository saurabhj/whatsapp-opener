#!/usr/bin/env python3

import sys
import webbrowser
import re

def sanitize_phone_number(phone_number):
    # Remove any non-numeric characters like spaces, dashes, pluses, etc.
    sanitized_number = re.sub(r'[^\d]', '', phone_number)

    # If the number is only 10 digits, add the country code '91'
    if len(sanitized_number) == 10:
        sanitized_number = '91' + sanitized_number

    return sanitized_number

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a phone number.")
        sys.exit(1)

    # Check if there are multiple arguments and join up to 3 parts for the phone number
    if len(sys.argv) > 2:
        phone_arg = ' '.join(sys.argv[1:min(4, len(sys.argv))])
    else:
        phone_arg = sys.argv[1]

    sanitized_number = sanitize_phone_number(phone_arg)

    # Ensure the phone number has been properly sanitized and opened appropriately
    whatsapp_url = f"https://web.whatsapp.com/send/?phone={sanitized_number}&text&type=phone_number&app_absent=1"
    
    print(f"Opening WhatsApp for phone number: {sanitized_number}")
    print(f"Opening URL: {whatsapp_url}")
    webbrowser.open(whatsapp_url)
