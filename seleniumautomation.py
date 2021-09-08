
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

# credentials
username = "pawanshejwal19@gmail.com"
with open('password.txt', 'r') as myfile:
         Password = myfile.read().replace('\n', '')
    

# initialize the Chrome driver
driver = webdriver.Chrome("./driver/chromedriver")
# head to wyscout login
driver.get("https://platformrc.wyscout.com/app/ ")
driver.implicitly_wait(30)
# find username/email field and send the username 

driver.find_element_by_id("login_username").send_keys(username)

# find password input field and insert password 

driver.find_element_by_id("login_password").send_keys(Password)
# click login button
driver.find_element_by_id("login_button").click()
time.sleep(40)
print("[+] Login successful")

# close the driver
driver.close()
