import bs4
from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://en.wikipedia.org/wiki/List_of_largest_employers'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html')

#print(soup)

#python webscraping_url.py

table = soup.find_all('table')[0]                              #getting table
#print(table)

head = table.find_all('th')                                    #getting all headlines with <th>
headings = [i.text.strip() for i in head]                      #headlines stored in list
print(headings)

df= pd.DataFrame(columns = headings)
#print(df)

row= table.find_all('tr')                                       #get all rows with <tr>
for rows in row[1:]:                                            #[1:] to escape empty 1st row
    raw=rows.find_all('td')                                     #get all rows with <td> having data
    row_data= [data.text.strip() for data in raw]               #.text to get text of the html
    length = len(df)                                            #looping data one by one in df using for loop
    df.loc[length]=row_data                                     # each row data inserted in df

print(df)

#converting to csv
df.to_csv('Largest_employers.csv', index= False)