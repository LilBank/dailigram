from selenium import webdriver
from selenium.webdriver.common.keys import keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time

class TestingWeb():
    
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome("chromedriver.exe")
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://dailigram.herokuapp.com/')
    driver = webdriver.Chrome()

    username = driver.find_element_by_xpath('//*[@id="id_username"]')
    password = driver.find_element_by_xpath('//*[@id="id_password"]')
    username.clear()
    username.send_keys('adminkit')
    password.send_keys('Kitcool@36')

    driver.find_element_by_name("login".click)

    # timeout = 5
    # try:
    #     element_present = EC.present_of_element_located(())