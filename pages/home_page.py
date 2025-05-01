from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.helps import wait_random
from utils.helps import move_mouse
from utils.helps import safe_send
from utils.helps import safeclick_cleanup

#Creation de class HomePgae && Initialization
class HomePgae:

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
    
    #Locators
    sign_in = (By.CSS_SELECTOR,".nav__button-secondary.btn-secondary-emphasis.btn-md")

    #signin pour passer en login

    def visible_Signin_click(self):
        wait_random(0.1,1.1)
        move_mouse(self.driver,self.sign_in)
        safeclick_cleanup(self.driver,self.sign_in)
        print("Page upload successful")


        










