from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from decouple import config




class TestingWeb(LiveServerTestCase):

    # def test_setUp(self):∫
    #     options = webdriver.ChromeOptions()
    #     options.add_argument("--start-maximized")
    #     options.add_argument('--ignore-certificate-errors')
    #     options.add_argument("--test-type")

        # options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        # self.driver = webdriver.Chrome("chromedriver.exe")
        # self.driver = webdriver.Chrome()
        # driver.set_window_size(1024, 600)
        # driver.maximize_window()
        # self.driver.get('https://dailigram.herokuapp.com/')
        # self.driver.close()

    # def test_search(self):
    #     username = driver.find_element_by_xpath('//*[@id="id_username"]')
    #     password = driver.find_element_by_xpath('//*[@id="id_password"]')
    #     username.clear()
    #     username.send_keys('admin')
    #     password.send_keys('admin1234')

    #     driver.find_element_by_name("login").click()
    #     driver.find_element_by_xpath("//nav/div/ul/li[4]/a").click()

    def setUp(self):
        self.selenium = webdriver.Chrome()
        super(TestingWeb, self).setUp()


    def test_register(self):
        selenium = self.selenium
        selenium.get('https://dailigram.herokuapp.com/')
        username = selenium.find_element_by_xpath('//*[@id="id_username"]')
        password = selenium.find_element_by_xpath('//*[@id="id_password"]')
        username.send_keys(config('TEST_USER'))
        password.send_keys(config('TEST_PASS'))
        selenium.find_element_by_name("login").click()
        # selenium.find_element_by_xpath("//nav/div/ul/li[4]/a").click()

    # def tearDown(self):
    #     self.selenium.quit()
    #     super(TestingWeb, self).tearDown()
    