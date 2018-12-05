from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from decouple import config
from selenium.webdriver.support.select import Select
import os




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
        options = webdriver.ChromeOptions()
        # options.binary_location = 'chromedriver.exe'
        # options.add_argument("--start-maximized")
        # options.add_argument('--ignore-certificate-errors')
        # options.add_argument('--test-type')
        # options.add_argument('--headless')
        # options.add_argument('--no-sandbox')
        # options.add_argument('--disable-gpu')
        # options.add_argument('--disable-dev-shm-usage')
        # options.binary_location = '/usr/bin/google-chrome-stable /usr/bin/X11/google-chrome-stable /usr/share/man/man1/google-chrome-stable.1.gz'
        self.selenium = webdriver.Chrome(chrome_options = options)
        super(TestingWeb, self).setUp()

    def test_alert(self):
        selenium = self.selenium
        selenium.maximize_window()
        selenium.get('https://dailigram.herokuapp.com/')
        username = selenium.find_element_by_xpath('//*[@id="id_username"]' )
        password = selenium.find_element_by_xpath('//*[@id="id_password"]')
        username.send_keys('testalert')
        password.send_keys('testalert')
        selenium.find_element_by_name("login").click()
        wait = WebDriverWait(driver, 3)
        selenium.wait.quit()

        # selenium.find_element_by_xpath("//nav/div/ul/li[4]/a").click()

    def test_inside(self):
        selenium = self.selenium
        selenium.maximize_window()
        selenium.get('https://dailigram.herokuapp.com/')
        username = selenium.find_element_by_xpath('//*[@id="id_username"]' )
        password = selenium.find_element_by_xpath('//*[@id="id_password"]')
        username.send_keys(config('TEST_USER'))
        password.send_keys(config('TEST_PASS'))
        selenium.find_element_by_name("login").click()
        selenium.find_element_by_xpath("//nav/div/ul/li[2]/a").click()
        title = selenium.find_element_by_id('id_title')      
        story = selenium.find_element_by_id('id_story')  
        title.send_keys('sample story')
        story.send_keys('This is an example story')
        mySelect = Select(selenium.find_element_by_id("id_tag"))
        mySelect.select_by_visible_text("Happy")
        # Imagepath = "Desktop\background-image-vertical-lines-and-stripes-seamless-tileable-black-white-22rjhc.png"
        selenium.find_element_by_xpath("//div[2]/h5/input").click()        
        selenium.find_element_by_xpath("//nav/div/ul/li[4]/a").click()
        wait = WebDriverWait(driver, 3)
        selenium.wait.quit()

        


