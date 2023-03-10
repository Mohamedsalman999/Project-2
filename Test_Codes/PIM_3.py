from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Test_Data import Data
from Test_Locators import Locators
import pytest

class Test_Salman:
       
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()
        
    
    # Test Login
    def test_Login(self, booting_function):
       self.driver.maximize_window()
       self.driver.get(Data.Salman_Data().url)
       sleep(5)
       self.driver.find_element(by=By.NAME, value=Locators.Salman_Locators().username_inputBox).send_keys(Data.Salman_Data().username)
       self.driver.find_element(by=By.NAME, value=Locators.Salman_Locators.password_InputBox).send_keys(Data.Salman_Data.password)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.LoginButton).click()
       assert self.driver.title == 'OrangeHRM'
       sleep(5)
       
    # click ths PIM 
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.PIM).click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.ADD).click()
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.Toggle).click()
       sleep(10)
       
    # create the new user and save 
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Firstname).send_keys(Data.Salman_Data().Firstname)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Middlename).send_keys(Data.Salman_Data().Middlename)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Lastname).send_keys(Data.Salman_Data().Lastname)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().emp_id).send_keys(Data.Salman_Data().emp_id)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Username).send_keys(Data.Salman_Data().Username)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Password).send_keys(Data.Salman_Data().Password)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().confirm).send_keys(Data.Salman_Data().confirm)
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.enable).click()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.save).click()
       sleep(5)
       
       