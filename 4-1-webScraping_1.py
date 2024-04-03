"""
Web Scraping
Extract all ads in divar.ir that includes 'نردبان'


Author: Mojtaba Hassanzadeh
Date: March 16, 2024
"""
import requests
from bs4 import BeautifulSoup

url = 'https://divar.ir/s/alvand'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# Find all span tags with class 'kt-post-card__red-text' containing the word 'نردبان'
target_spans = soup.find_all('span', class_='kt-post-card__red-text', string=lambda string: string and 'نردبان' in string)
# or target_spans = soup.find_all('span', class_='kt-post-card__red-text', string=lambda x: x and 'نردبان' in x)

for span in target_spans:
    # Get the parent tag of the span tag
    parent_tag = span.find_parent('div', class_='kt-post-card__info')

    if parent_tag:
        # Extract the necessary information from the parent tag
        product_title = parent_tag.find('h2', class_='kt-post-card__title').text.strip()
        product_description = parent_tag.find_all('div', class_='kt-post-card__description')
        price = product_description[1].text.strip() if len(product_description) >= 2 else "Price not available"
       
        # Print the extracted information
        print(f"Product Title: {product_title}")
        print(f"Price: {price}") 
        print("--------")