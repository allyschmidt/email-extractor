import os
import email
from email import policy

email_dir = "emails"
x = True # temporary variable for the while loop

def get_email_body(msg): # extract the body of the email
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":  # only get plain text emails
                return part.get_payload(decode=True).decode()
            
    else:
        return msg.get_payload(decode=True).decode()

# for each file in the email directory, get the filepath and message
for file in os.listdir(email_dir): 
    filepath = os.path.join(email_dir, file)
    print(filepath)

    with open(filepath, "r", encoding="utf-8") as eml_file:
        msg = email.message_from_file(eml_file, policy=policy.default)

    while (x): # print details of one email for testing purposes
        subject = msg["Subject"]
        sender = msg["From"]
        date = msg["Date"]
        body = get_email_body(msg)

        print(f"Subject: {subject}")
        print(f"From: {sender}")
        print(f"Date: {date}")
        print(f"Body: {body}")
        x = False
