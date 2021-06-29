import selenium
from selenium import webdriver
import time
import creds



username = creds.login['OL_USERNAME']
password = creds.login['OL_PASSWORD']

# Using Chrome to access web
driver = webdriver.Chrome('./chromedriver')

# Open the site
driver.get('https://www.overleaf.com/login')

time.sleep(1)
# Select id and password boxes
id_box = driver.find_element_by_name('email')
pass_box = driver.find_element_by_name('password')
login_box = driver.find_element_by_xpath('/html/body/div/main/div/form/div[3]/button/span[1]')

# send id and password
id_box.send_keys(username)
pass_box.send_keys(password)

login_box.click()
time.sleep(3)
# Download coursework project
projects = ['5ffb88cff3c28ff81e003cb8']
for uid in projects:
    driver.get(f'https://www.overleaf.com/project/{uid}/download/zip')
    time.sleep(5)

driver.quit()
