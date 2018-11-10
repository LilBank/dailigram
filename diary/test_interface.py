from django.test import TestCase
from django.urls import reverse
from diary.models import Page, Diary
# from django import forms
# from diary.forms import UserForm
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


# class TestingWeb():

    
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#     options.add_argument('--ignore-certificate-errors')
#     options.add_argument("--test-type")
    

#     options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
#     driver = webdriver.Chrome("chromedriver.exe")
#     driver.set_window_size(1024, 600)
#     driver.maximize_window()
#     driver.get('https://dailigram.herokuapp.com/')

#     username = driver.find_element_by_xpath('//*[@id="id_username"]')
#     password = driver.find_element_by_xpath('//*[@id="id_password"]')
#     username.clear()
#     username.send_keys('adminkit')
#     password.send_keys('kit12345')

#     driver.find_element_by_name("login").click()
#     driver.find_element_by_xpath("//nav/div/ul/li[4]/a").click()   