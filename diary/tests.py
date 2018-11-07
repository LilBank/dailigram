from django.test import TestCase
from django.urls import reverse
from diary.models import Page, Diary
from django import forms
from diary.forms import UserForm
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



# class TestingModels(TestCase):

#     def test_diary_pk(self):
#         """
#         Test that the primary key should be one for each object's creation.
#         """
#         diary = Diary.objects.create(first_name='tintin')
#         self.assertEqual(diary.pk, 1)

#     def test_string_representation(self):
#         """
#         Test that the string is correctly represented.
#         """
#         diary = Diary.objects.create(first_name='tintin')
#         self.assertEqual(str(diary), diary.first_name)

#     def test_diary_max_length(self):
#         """
#         Test that the max length of the field is equal or not.
#         """
#         diary = Diary(first_name='tony')
#         max_length = diary._meta.get_field('first_name').max_length
#         self.assertEquals(max_length, 100)

#     def test_no_diary_by_model(self):
#         """
#         Test that the total number of object is 0 when nothing is created.
#         """
#         num_diary = Diary.objects.all().count()
#         self.assertEqual(num_diary, 0)


# class TestingViews(TestCase):

#     def test_accessible_by_name(self):
#         """
#         Test diary's existance by the response status code.
#         """
#         response = self.client.get(reverse('login'))
#         self.assertEqual(response.status_code, 200)

#     def test_accessible_by_location(self):
#         response = self.client.get('/accounts/diary/')
#         self.assertEqual(response.status_code, 200)

#     def test_no_diary_by_view(self):
#         """
#         Test that the total context object is 0 when nothing is inserted.
#         """
#         response = self.client.get(reverse('diary:login'))
#         self.assertQuerysetEqual(response.context['all_diarys'], [])
    
#     def test_login(self):
#         """
#         Test if the login is sucess or not
#         """
#         response = self.client.post('/accounts/login/', self.credentials, follow=True)
#         self.assertTrue(response.context['user'].is_authenticated)

# class TestingForms(TestCase):

#     def test_valid_forms(self):
#         """
#         Test if the form is valid or not.
#         """
#         form  = UserForm()
#         self.assertTrue(form.is_valid)

    
class TestingWeb():
    
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--test-type")
    options.binary_location = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(chrome_options=options)
    driver.get('https://dailigram.herokuapp.com/')
    driver = webdriver.Chrome()

    username = driver.find_element_by_xpath('//*[@id="id_username"]')
    password = driver.find_element_by_xpath('//*[@id="id_password"]')
    username.clear()
    username.send_keys('adminkit')
    password.send_keys('Kitcool@36')

    driver.find_element_by_name("login".click)

    
        





