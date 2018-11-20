from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options




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
