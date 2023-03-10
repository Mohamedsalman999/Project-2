from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
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
       sleep(3)
       
    # click the search box and validate the all metioned test with upper and lower cases
    
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_1)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_11)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_2)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_22)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_33)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_4)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_44)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_5)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_55)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_6)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_66)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_7)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_77)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_8)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_88)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_9)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_99)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_10)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_1010)
       sleep(3)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_110)
       element = self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search)
       action = ActionChains(self.driver)
       action.double_click(on_element = element).perform()
       self.driver.find_element(by=By.XPATH, value=Locators.Salman_Locators().search).send_keys(Data.Salman_Data().search_1111)
       sleep(3)

