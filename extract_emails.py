import re

def get_email_sections(email_body):
    headers = []

    split_body = email_body.split("\n")
    for line in split_body:
        if line in headers:
            break
        headers.append(line.strip())
        split_body = split_body[1:]

    split_body = "\n".join(split_body)

    sections = re.split(r"(?m)^(" + "|".join(headers) + r")$", split_body)
    return [item for item in sections if item], headers


def extract_entries(category, section, date):

    entries = []
    
    pattern = re.compile(r"(.+?)\s*--\s*Submitted by:\s*([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})\s*(.+?)\s*More Information...")

    for match in pattern.finditer(section):

        item_name = match.group(1).strip()
        user_email = match.group(2).strip()
        message = match.group(3).strip()

        price_match = re.search(r"\$([\d,]+(?:\.\d{1,2})?)", item_name)

        if not price_match:
            price_match = re.search(r"\$([\d,]+(?:\.\d{1,2})?)", message)
        
        price = float(price_match.group(1).replace(",", "")) if price_match and category in["Marketplace", "Rental/Roommates"] else None
        
        entries.append({"Category":category, "Item": item_name, "Price": price, "User": user_email, 
                        "Date": date, "Description": message})

    return entries