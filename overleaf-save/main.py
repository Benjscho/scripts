import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import creds

username = creds.login['OL_USERNAME']
password = creds.login['OL_PASSWORD']

# Using Chrome to access web
driver = webdriver.Chrome('./chromedriver')

# Open the site
driver.get('https://www.overleaf.com/login')

# Select id and password boxes
id_box = driver.find_element_by_name('email')
pass_box = driver.find_element_by_name('password')
login_box = driver.find_element_by_xpath('/html/body/div/main/div/form/div[3]/button/span[1]')

# send id and password
id_box.send_keys(username)
pass_box.send_keys(password)

login_box.click()
time.sleep(1)
# Download coursework project
driver.get('https://www.overleaf.com/project/5f76e2c5ebfaed00018ea900/download/zip')
time.sleep(1)

driver.quit()
