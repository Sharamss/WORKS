import csv
import os
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from fake_useragent import UserAgent


# Configuration
url = 'https://www.undp.org/nepal/projects'
output_file = 'UNDP.csv'
directory = 'ProjectData'
full_path = os.path.join(directory, output_file)
headers = ['Name of the Project', 'Link to the project']

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Initialize the web driver (choose the appropriate driver for your browser)
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
#options.add_argument('--headless=new')
options.add_argument(f'--user-agent={UserAgent().random}')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open the webpage
driver.get(url)

# Work with the CSV file
with open(full_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    while True:
        try:
            
            page = driver.page_source
            page_soup = soup(page, 'html.parser')

            containers = page_soup.findAll('div', {'class': 'content-card'})
            for container in containers:
                if container.find('a'):
                    link = container.a.get('href', '')
                    project_link = 'https://www.undp.org' + link
                    project_name = container.find('h5').text.strip() if container.find('h5') else 'No title available'

                    writer.writerow([project_name, project_link])
                    
            # Attempt to click the 'See More' button if it exists
            viewbtn_xpath = '/html/body/div[1]/main/div/div/div[2]/article/div/div/section/div[1]/div/div[2]/div[2]/div[1]/button'
            button = driver.find_element(By.XPATH, viewbtn_xpath) if driver.find_elements(By.XPATH, viewbtn_xpath) else None
            if button:
                ActionChains(driver).move_to_element(button).click(button).perform()
                time.sleep(2)
            else:
                break
            
            body = driver.find_element(By.TAG_NAME, 'body')
            body.send_keys(Keys.END)
            body.send_keys(Keys.PAGE_UP)
            time.sleep(5)
                    
        except Exception as e:
            print(f"An error occurred: {e}")
            break

driver.quit()