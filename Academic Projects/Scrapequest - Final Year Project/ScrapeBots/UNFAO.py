import csv
import os
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

# Configuration
url = 'https://www.fao.org/nepal/programmes-and-projects/project-list/ru/?no_cache=1'
output_file = 'UNFAO.csv'
directory = 'ProjectData'
full_path = os.path.join(directory, output_file)
headers = ['Name of the Project', 'Duration of the Project', 'Link to the project']

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Initialize the web driver (choose the appropriate driver for your browser)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless=new')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open the webpage
driver.get(url)

# Work with the CSV file
with open(full_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    try:      
        while True:
            page = driver.page_source
            page_soup = soup(page, 'html.parser')
            containers = page_soup.findAll('div', {'class': 'rgaccord1-nest'})

            if not containers:
                break  # If no more projects found, break the loop

            for container in containers:
                h3 = container.find('h3', {'class':'rgaccord1-toggle'})
                project_name = h3.text.strip() if h3 else 'No title available'

                content = container.find('div', {'class':'csc-default'})
                project_desc = content.text.strip() if content else 'Description not available'
                match = re.search(r'Period:(.*)', project_desc)
                period = match.group(1).strip() if match else 'No period available'

                project_link = 'https://www.fao.org/nepal/programmes-and-projects/project-list/ru/?no_cache=1'

                # Write to CSV
                writer.writerow([project_name, period, project_link])


            break
            
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        driver.quit()
