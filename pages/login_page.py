from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Email, Password
from utils.helps import wait_random
from utils.helps import move_mouse
from utils.helps import safe_send
from utils.helps import safeclick_cleanup
import time
import os

class Loginpage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    
    #Création login Class
    user_name = (By.ID,"username")
    key_word = (By.ID,"password")
    signin_boutton = (By.CSS_SELECTOR,".btn__primary--large.from__button--floating")

    #full login information
    def full_email_key_work(self):
        email = os.getenv("LINKEDIN_EMAIL")
        password = os.getenv("LINKEDIN_PASSWORD")
        
        email_input = self.wait.until(EC.presence_of_element_located(self.user_name))
        email_input.send_keys(email)
        print("📧 Email correct")

        password_input = self.wait.until(EC.presence_of_element_located(self.key_word))
        password_input.send_keys(password)
        print("🔐 Password correct")

        self.driver.save_screenshot("screenshots/fill_login.png")



    def signin_button_click(self):
        button = self.wait.until(EC.element_to_be_clickable(self.signin_boutton))
        button.click()
        print("✅ Click sur Sign in effectué")
        time.sleep(3)
        print("🔗 URL après login:", self.driver.current_url)
        self.driver.save_screenshot("screenshots/after_login.png")


    

