import csv
import os
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configuration
url = 'https://projects.worldbank.org/en/projects-operations/procurement?srce=both'
directory = './ProjectData'
output_file = 'WB.csv'
full_path = os.path.join(directory, output_file)
headers = ['Name of the Project', 'Link to the project', 'Procurement Details', 'Link to the Procurement', 'Date of Publishment']

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Initialize the web driver (choose the appropriate driver for your browser)
options = webdriver.ChromeOptions()
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

# Initialize and click filters and buttons using XPath
try:
    filter_button_Xpath = "/html/body/div[3]/div[2]/div[2]/div[2]/procurement-search/div/div/div/procurement-facets/div/div/div/ul[1]/li/a"
    filter_button = driver.find_element(By.XPATH, filter_button_Xpath)
    ActionChains(driver).scroll_to_element(filter_button).click(filter_button).perform()
    time.sleep(1)

    see_more_btn_xpath = "/html/body/div[3]/div[2]/div[2]/div[2]/procurement-search/div/div/div/procurement-facets/div/div/div/ul[1]/ul/li[170]/a"
    see_more_btn = driver.find_element(By.XPATH, see_more_btn_xpath)
    ActionChains(driver).scroll_to_element(see_more_btn).click(see_more_btn).perform()
    time.sleep(1)

    nepal_btn_xpath = "/html/body/div[3]/div[2]/div[2]/div[2]/procurement-search/div/div/div/procurement-facets/div/div/div/ul[1]/ul/li[34]/div/input"
    nepal_btn = driver.find_element(By.XPATH, nepal_btn_xpath)
    ActionChains(driver).scroll_to_element(nepal_btn).click(nepal_btn).perform()
    time.sleep(1)

    # Writing to file
    with open(full_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        
        while True:
            page = driver.page_source
            page_soup = soup(page, 'html.parser')
            containers = page_soup.findAll('tr', {'class': 'ng-star-inserted'})
            
            for container in containers:
                procurement = container.find('td')
                procurement_link = 'https://projects.worldbank.org' + procurement.a['href']
                procurement_desc = procurement.a.text.strip()
                
                project = container.find('td', {'data-th': 'Project Title:'})
                project_link = 'https://projects.worldbank.org' + project.a['href']
                project_desc = project.a.text.strip()
                
                published_date = container.find('td', {'data-th': 'Published Date:'}).text.strip()
                
                writer.writerow([project_desc, project_link, procurement_desc, procurement_link, published_date])
            
            next_button_xpath = "/html/body/div[3]/div[2]/div[2]/div[2]/procurement-search/div/div/div/div/div[1]/div/section/tabset/section/div/projects-tab[1]/table-api/div[1]/div/div[2]/div/ul/li[13]/a/i"
            next_button = driver.find_element(By.XPATH, next_button_xpath) if driver.find_elements(By.XPATH, next_button_xpath) else None
            if next_button: 
              ActionChains(driver).scroll_to_element(next_button).click(next_button).perform()
              time.sleep(1)
            else:
              break
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
