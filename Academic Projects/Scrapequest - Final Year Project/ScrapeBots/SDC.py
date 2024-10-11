import csv
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

# Configuration
base_url = 'https://www.eda.admin.ch/countries/nepal/en/home/international-cooperation/projects.olddesign.olddesign.olddesign.olddesign.olddesign.par_projectfilter_2b80_page{}.html'
directory = 'ProjectData'
output_file = 'SDC.csv'
full_path = os.path.join(directory, output_file)
headers = ['Name of the Project', 'Link to the project', 'Duration of the Project', 'Project Details']
max_page_num = 7  # Adjust the max page number as per requirement

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
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(300)

# Open the webpage and parse projects
try:
    with open(full_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

        for page_num in range(1, max_page_num + 1):
            url = base_url.format(page_num)
            driver.get(url)
            time.sleep(5)  # Wait for the page to load
            page_soup = soup(driver.page_source, 'html.parser')
            
            containers = page_soup.find_all('article', class_='clearfix')
            for container in containers:
                if container.find('h4'):
                    h4_tag = container.find('h4')
                    a_tag = h4_tag.find('a') if h4_tag else None
                    project_name = a_tag.text.strip() if a_tag else 'N/A'
                    project_link = 'https://www.eda.admin.ch' + a_tag['href'] if a_tag else 'N/A'
                    project_duration = container.find('small').text.strip() if container.find('small') else 'N/A'
                    project_description = ' '.join([strong.text.strip() for strong in container.find_all('strong')]) if container.find_all('strong') else 'N/A'
                    
                    # Write to CSV
                    writer.writerow([project_name, project_link, project_duration, project_description])

finally:
    driver.quit()
