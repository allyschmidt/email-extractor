import email
from email import policy
import chardet
from bs4 import BeautifulSoup
from email.utils import parsedate_to_datetime


def get_email_body(msg): # extract the body of the email
    body = msg.get_payload(decode=True).decode()

    soup = BeautifulSoup(body, "html.parser")
    clean_text = soup.get_text(separator="\n", strip=True)
    
    return(clean_text)


def get_email_date(msg):
    date_header = msg["Date"]
    if date_header:
        date = parsedate_to_datetime(date_header)  # Converts to datetime
        converted_date = f"{date.month}/{date.day}/{date.year}"
        return converted_date
    return None


def load_email(filepath):

    with open(filepath, 'rb') as eml_file:  # Open in binary mode
        raw_data = eml_file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding'] if result['encoding'] else 'utf-8'

    email_data = raw_data.decode(encoding, errors='ignore')
    msg = email.message_from_string(email_data, policy=policy.default)

    return get_email_body(msg), get_email_date(msg)
