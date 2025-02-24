import os
from read_emails import *
from extract_marketplace import *
import csv

email_dir = "emails"
csv_headers = ["Category", "Item", "Price", "User", "Date", "Description"]

university_data = []
departmental_data = []
marketplace_data = []
student_org_data = []
roommate_data = []
general_data = []


for file in os.listdir(email_dir):

    filepath = os.path.join(email_dir, file)
    email_body, date = load_email(filepath)
    sections, headers = get_email_sections(email_body)
    x=True

    for current_section, next_section in zip(sections, sections[1:]):

        match current_section:
            case "University Announcements":
                university_items = extract_entries("University Announcements", next_section, date)
                university_data.extend(university_items)
            case "Department Announcements":
                department_items = extract_entries("Department Announcements", next_section, date)
                departmental_data.extend(department_items)
            case "Marketplace":
                marketplace_items = extract_entries("Marketplace", next_section, date)
                marketplace_data.extend(marketplace_items)
            case "Student Organizations":
                student_org_items = extract_entries("Student Organizations", next_section, date)
                student_org_data.extend(student_org_items)
            case "Rental/Roommates":
                roommate_items = extract_entries("Rental/Roommates", next_section, date)
                roommate_data.extend(roommate_items)
            case "General Announcements":
                general_items = extract_entries("General Announcements", next_section, date)
                general_data.extend(general_items)

    
filename = 'all_items.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=csv_headers)
    writer.writeheader()

    writer.writerows(item for item in university_data)
    writer.writerows(item for item in departmental_data)
    writer.writerows(item for item in marketplace_data)
    writer.writerows(item for item in student_org_data)
    writer.writerows(item for item in roommate_data)
    writer.writerows(item for item in general_data)
