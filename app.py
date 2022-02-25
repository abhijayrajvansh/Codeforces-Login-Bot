#/
#    author:   abhijayrajvansh
#    created:  25.02.2022 17:50:25
#/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options #to by-pass chrome broswer notification
from selenium.webdriver.common.by import By

import os
import datetime
import time

pwd = os.getcwd()
PATH = Service(pwd + "/chromedriver")

# url to be launched ...
url = "https://codeforces.com/"

# Handling Chrome Options:
chromeOptions = Options()
chromeOptions.add_argument("--disable-extensions")
chromeOptions.add_argument("--disable-notifications")
# chromeOptions.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2 }) 

# driver setup:
driver = webdriver.Chrome(service = PATH, options = chromeOptions)
driver.maximize_window()
# driver.minimize_window()

driver.get(url) # launches the broswer and open url
time.sleep(1) # very important everything to load before exicuting commands // safe at 5

username = "" # Enter your username/email ID here
password = "" # Enter your password ID here

def login():
    global ID
    global ps
    driver.find_element(By.XPATH, "//a[normalize-space()='Enter']").click()
    driver.find_element(By.XPATH, "//input[@id='handleOrEmail']").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//input[@id='remember']").click()
    driver.find_element(By.XPATH, "//input[@value='Login']").click()
    print("`````````````````````````````````````````````")
    print("| Successfully Logged In To Codeforces Acc! |")
    print(",,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,")

login();

time.sleep(5);

