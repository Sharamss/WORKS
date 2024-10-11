import csv
import os
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

# Configuration
url = 'https://devtracker.fcdo.gov.uk/countries/NP/projects#/'
directory = 'ProjectData'
output_file = 'UKAID.csv'
full_path = os.path.join(directory, output_file)
headers = ['Name of the Project', 'Link to the project', 'Project Details', 'Start Date']

# Ensure the directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Set up Selenium WebDriver with Chrome
options = Options()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')
options.add_argument('--start-maximized')
options.add_argument('--disable-web-security')
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(300)

# Open the webpage
driver.get(url)
time.sleep(2)

# Work with the CSV file
with open(full_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    while True:
        try:
            # Click all "Read More" buttons to reveal full project descriptions
            read_more_buttons = driver.find_elements(By.CSS_SELECTOR, ".rm-link")
            for button in read_more_buttons:
                try:
                    driver.execute_script("arguments[0].scrollIntoView(true);", button)
                    driver.execute_script("arguments[0].click();", button)
                    time.sleep(1)  # Wait for potential dynamic content
                except Exception as e:
                    print(f"Error clicking a 'Read More' button: {e}")
            
            page = driver.page_source
            page_soup = soup(page, 'html.parser')
            project_containers = page_soup.find('div', id='response-container')
            containers = project_containers.find_all('div', class_='app-search-result')

            for container in containers:
                project_title_container = container.find('h3', class_='govuk-heading-s app-search-result-title')
                name = project_title_container.text.strip()
                link = project_title_container.find('a', class_='govuk-link--no-visited-state')['href']
                full_link = "https://devtracker.fcdo.gov.uk" + link

                info_divs = container.find_all('div', class_='app-search-result-info')
                start_date = ""
                for info_div in info_divs:
                    info_pairs = info_div.find_all('div')
                    for pair in info_pairs:
                        title = pair.find('span', class_='govuk-body-s app-search-result-info__title').text.strip()
                        value = pair.find('span', class_='govuk-body-s app-search-result-info__value').text.strip()
                        if title == "Start date":
                            start_date = value
                            break
                    if start_date:
                        break

                description = container.find('p', class_='govuk-body-s description').text.strip()
                writer.writerow([name, full_link, description, start_date])

            # Check for and click the "Next" button, if present
            next_btn_xpath = "/html/body/div[5]/main/div[4]/div[2]/div[3]/ul/li[8]/a"
            next_btn = driver.find_element(By.XPATH, next_btn_xpath) if driver.find_elements(By.XPATH, next_btn_xpath) else None
            if next_btn:
                ActionChains(driver).move_to_element(next_btn).click(next_btn).perform()
                time.sleep(4)
            else:
                break
        except Exception as e:
            print(f"An error occurred: {e}")
            break

driver.quit()
