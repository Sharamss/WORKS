import csv
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import re
import pandas as pd
import os

# Configuration
url = 'https://www.jica.go.jp/english/overseas/nepal/activities/index.html'
output_file = 'JICA.csv'
directory = 'ProjectData'
full_path = os.path.join(directory, output_file)
headers = ['Name of the Project', 'Link to the project']

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)
    
# Set up Selenium WebDriver with Chrome
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless=new')
options.add_argument('--start-maximized')
options.add_argument('--disable-web-security')
options.add_argument('user-agent=fake-useragent')
options.add_argument('--disable-gpu')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(300)

# Open the webpage
driver.get(url)
page = driver.page_source

# Parse the page
page_soup = soup(page, 'html.parser')
projects = page_soup.findAll('div', {'class': 'discList'})

# Prepare to write to CSV
with open(full_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    for container in projects:
        project_name = container.find('li').text.strip()
        project_links = [link['href'] for link in container.find_all('a') if 'href' in link.attrs]
        project_links = [f'https://www.jica.go.jp{link}' if link.startswith('/') else link for link in project_links]

        # Write to CSV
        writer.writerow([project_name, project_links])

# Clean up
driver.quit()

