# Marketplace Listing Analysis

## Project Overview
This project analyzes the contents of marketplace .eml files to identify item posting trends.  Using Python, it extracts data such as what user posted the item, the price and date, as well as what category each item was posted under.  The purpose of this project was to discover whether certain items were posted more during specific times of the year.

## Background
The motivation for this project stemmed from the desire to see whether my college marketplace had listings about textbook sales year round.  I accumulated many textbooks since starting college, and I wanted to know whether or not textbooks had a noticeable spike in listings at different points in the year.  I expanded the project to include the other types of listings. Textbook listings are typically listed under "Marketplace," but I decided to add the other categories such as "Rental/Roommates," "University Announcements," and "Student Organizations."

## Current Implementation
Currently, the project extracts item listings from each email and creates a CSV file containing the listing and pertinent information.  The file "data_analysis.py" cleans the data and displays initial visualizations.  These include a price analysis of both the "Marketplace" and "Rental/Roommates" categories.

## Usage
Running the file "main.py" with an appropriate folder "emails" containing appropriate .eml files results in an "all_items.csv" being created with the extracted data.  The file "data_analysis.py" imports "all_items.csv" and handles exploratory data analysis, data cleaning, insights into the dataset, and visualizations.

## Future Improvements
- Implementing a procedure that categorizes listings by type (clothing, books, sublease announcement, etc)
- Adding a visualization that characterizes listings by the date they were posted to identify posting trends
- Adding additional visualizations that show user posting trends, pricing trends, and what types of listings are most common
