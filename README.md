# Webscraping-largest-employer
📌 Wikipedia Web Scraper: Largest Employers

📖 Project Overview

This Python project scrapes data from a Wikipedia page that lists the largest employers in the world and saves the extracted data into a CSV file.

🔗 Target URL: Wikipedia - Largest Employers

🔧 Features

✅ Scrapes data from Wikipedia using BeautifulSoup✅ Extracts table data including company names, employee counts, industry types, etc.✅ Cleans and processes the extracted data✅ Converts the data into a pandas DataFrame✅ Saves the data as a CSV file (Largest_employers.csv)

🛠️ Setup and Installation

Step 1: Install Required Libraries

Before running the script, install the necessary dependencies:

pip install requests beautifulsoup4 pandas

Step 2: Run the Python Script

python webscraping_url.py

Step 3: Check the Output

The extracted data will be printed in the terminal

A CSV file Largest_employers.csv will be created with the extracted data

📜 Code Explanation

1️⃣ Importing Required Libraries

import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

requests: Fetches the Wikipedia page content

BeautifulSoup: Parses the HTML content

pandas: Stores and processes the extracted data

2️⃣ Fetching the Wikipedia Page

url = 'https://en.wikipedia.org/wiki/List_of_largest_employers'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')

Fetches the HTML content from the Wikipedia page

Parses the page using BeautifulSoup

3️⃣ Extracting the Table Data

table = soup.find_all('table')[0]  # Selecting the first table

Wikipedia pages contain multiple tables; the script selects the first table (table[0]).

4️⃣ Extracting Column Headers

head = table.find_all('th')
headings = [i.text.strip() for i in head]  # Strip removes newline characters
print(headings)

Extracts column headers from the table and cleans them.

5️⃣ Creating a Pandas DataFrame

df = pd.DataFrame(columns=headings)
print(df)

Creates an empty DataFrame with the extracted column headers.

6️⃣ Extracting Row Data

row = table.find_all('tr')
for rows in row[1:]:  # Skipping the first row to remove empty rows
    raw = rows.find_all('td')
    row_data = [data.text.strip() for data in raw]
    length = len(df)
    df.loc[length] = row_data

Iterates over the table rows and extracts data cell by cell.

Removes empty rows and appends data to the DataFrame.

7️⃣ Saving Data to CSV File

df.to_csv('Largest_employers.csv', index=False)

Saves the scraped data into a CSV file named Largest_employers.csv.
