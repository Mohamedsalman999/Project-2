from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
       
    # click the PIM
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.PIM).click()
       sleep(10)
       
    # search the created new user in PIM_3 by id number
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Emp_id).send_keys(Data.Salman_Data().Emp_id)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.Search).click()
       sleep(5)
       self.driver.execute_script("window.scrollBy(0,2000)","")
       sleep(5)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.userlist).click()
       sleep(5)
       
    # update the salary details and validate the updated salary details
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.salary).click()
       sleep(2) 
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.Add_2).click()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().component).send_keys(Data.Salman_Data().component)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().pay_frequency).click()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().pay_frequency).send_keys(Data.Salman_Data().pay_frequency)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().pay_frequency).send_keys(Keys.ENTER)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().currency).click()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().currency).send_keys(Data.Salman_Data().currency)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().currency).send_keys(Data.Salman_Data().currency)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().currency).send_keys(Data.Salman_Data().currency)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().currency).send_keys(Keys.ENTER)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().amount).send_keys(Data.Salman_Data().amount)
       sleep(4)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().save_6).click()
       sleep(6)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().edit).click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Toggle_2).click()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().acc_num).send_keys(Data.Salman_Data().acc_num)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().acc_type).click()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().acc_type).send_keys(Data.Salman_Data().acc_type)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().acc_type).send_keys(Keys.ENTER)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().routing_num).send_keys(Data.Salman_Data().routing_num)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().amount_1).send_keys(Data.Salman_Data().amount_1)
       sleep(4)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().save_7).click()
       sleep(6)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().salary).click()
       sleep(4)
       
       
       
       