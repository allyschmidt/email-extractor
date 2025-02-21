import os
import email
from email import policy

email_dir = "emails"
x = True

def get_email_body(msg):
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":  # Only get plain text emails
                print("AAA")
                return part.get_payload(decode=True).decode()
            
    else:
        print("BBB")
        return msg.get_payload(decode=True).decode()


for file in os.listdir(email_dir):
    filepath = os.path.join(email_dir, file)
    print(filepath)

    with open(filepath, "r", encoding="utf-8") as eml_file:
        msg = email.message_from_file(eml_file, policy=policy.default)

    while (x):
        subject = msg["Subject"]
        sender = msg["From"]
        date = msg["Date"]
        body = get_email_body(msg)

        print(f"Subject: {subject}")
        print(f"From: {sender}")
        print(f"Date: {date}")
        print(f"Body: {body}")


        x = False
