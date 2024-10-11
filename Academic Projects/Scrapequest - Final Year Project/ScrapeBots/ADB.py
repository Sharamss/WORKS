import csv
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import time
import os

# Configuration
url_template = 'https://www.adb.org/projects/tenders/country/nepal?page={}'
output_file = 'ADB.csv'
directory = 'ProjectData'
full_path = os.path.join(directory, output_file)
headers = ['Name of the Project', 'Link to the project', 'Project Status', 'Project Description']

# Set up Selenium WebDriver with Chrome
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--start-maximized')
options.add_argument('--disable-web-security')
options.add_argument(f'--user-agent={UserAgent().random}')
options.add_argument('--disable-gpu')
options.add_argument('--headless=new')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(300)

# Open the output file and write headers
with open(full_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    page_num = 0
    while page_num<=16:
        try:
            # Load the page
            driver.get(url_template.format(page_num))
            time.sleep(5)  # Wait for the page to load

            # Parse the page
            page_soup = soup(driver.page_source, 'html.parser')
            containers = page_soup.findAll('div', {'class': 'item linked'})

            if not containers:
                print("No more projects found.")
                break  # Exit the loop if no containers are found

            # Process each project
            for container in containers:
                title = container.find('div', {'class': 'item-title'}).a
                project_title = title.text.strip()
                project_link = "https://adb.org/" + title['href']
                project_status = container.find('div', {'class': 'item-meta'}).div.text.strip()
                project_description = container.find('div', {'class': 'item-summary'}).text.strip()

                # Write project details to CSV
                writer.writerow([project_title, project_link, project_status, project_description])

            page_num += 1  # Increment page number for the next page

        except Exception as e:
            print(f"Error occurred: {e}")
            break

# Quit the driver after the loop
driver.quit()
