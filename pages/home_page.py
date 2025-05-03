from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.helps import wait_random
from utils.helps import move_mouse
from utils.helps import safe_send
from utils.helps import safeclick_cleanup
import random
import time

#Creation de class HomePgae && Initialization
class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.sign_in = (By.CSS_SELECTOR, ".nav__button-secondary.btn-secondary-emphasis.btn-md")
    
    #Locators
    sign_in = (By.CSS_SELECTOR,".nav__button-secondary.btn-secondary-emphasis.btn-md")

    #signin pour passer en login

    def visible_Signin_click(self):
    wait_random(0.1, 1.1)
    element = self.wait.until(EC.presence_of_element_located(self.sign_in))
    move_mouse(self.driver, element)
    safeclick_cleanup(self.driver, element)
    print("Page upload successful")