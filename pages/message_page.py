from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.helps import safe_send
from utils.helps import safeclick_cleanup
from utils.helps import wait_random
from utils.helps import move_mouse

class Message:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    
    #Locators
    champ_message=(By.CSS_SELECTOR,"div.msg-form__contenteditable[contenteditable='true']")
    envoyer=(By.CSS_SELECTOR,".msg-form__send-button.artdeco-button.artdeco-button--1")

    def fill_message_send(self,value):
        move_mouse(self.driver,self.champ_message)
        safe_send(self.champ_message,"Hbiba dyali, Tanmout Fik")
        move_mouse(self.driver,self.envoyer)
        safeclick_cleanup(self.driver,self.envoyer)
        wait_random(0.1,2)
