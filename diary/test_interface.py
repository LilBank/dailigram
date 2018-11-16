from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By


class TestingWeb():

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")

        # options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        # self.driver = webdriver.Chrome("chromedriver.exe")
        self.driver = webdriver.Chrome()
        # driver.set_window_size(1024, 600)
        # driver.maximize_window()
        driver.get('https://dailigram.herokuapp.com/')

    def test_search(self):
        username = driver.find_element_by_xpath('//*[@id="id_username"]')
        password = driver.find_element_by_xpath('//*[@id="id_password"]')
        username.clear()
        username.send_keys('admin')
        password.send_keys('admin1234')

        driver.find_element_by_name("login").click()
        driver.find_element_by_xpath("//nav/div/ul/li[4]/a").click()

        # driver.close()

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
