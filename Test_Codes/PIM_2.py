from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from Test_Locators import Locators
from Test_Data import Data
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
       
    # validate the admin page
    
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Admin).click()
       sleep(3)
       
    # click the user management and user
       
       User_management = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().User_management)
       sleep(2)
       User_management.click()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Users).click()
       sleep(3)
       
    # validate the user role and user status
    
       User_role = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().User_role)
       sleep(2)
       User_role.click()
       User_status = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().User_status)
       sleep(2)
       User_status.click()
       
       