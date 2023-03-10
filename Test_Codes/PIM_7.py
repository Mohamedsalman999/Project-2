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
       
    # update the emergency details    
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.emergency).click()
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.Add).click()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Rlt_name).send_keys(Data.Salman_Data().Rlt_name)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Relation).send_keys(Data.Salman_Data().Relation)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Home_num).send_keys(Data.Salman_Data().Home_num)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().save_2).click()
       sleep(5)
       
    # validate the updated emergency details   
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().PIM).click()
       sleep(3)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().Emp_id).send_keys(Data.Salman_Data().Emp_id)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.Search).click()
       sleep(2)
       self.driver.execute_script("window.scrollBy(0,2000)","")
       sleep(2)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.userlist).click()
       sleep(3)
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators.emergency).click()
       sleep(2)   