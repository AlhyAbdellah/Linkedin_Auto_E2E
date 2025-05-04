from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config import Email, Password
from utils.helps import wait_random
from utils.helps import move_mouse
from utils.helps import safe_send
from utils.helps import safeclick_cleanup

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
        wait_random(0.5, 1.1)
        email_field = self.wait.until(EC.presence_of_element_located(self.user_name))
        move_mouse(self.driver, email_field)
        safe_send(email_field, Email)
        print("email correct")

        wait_random(0.5, 1.1)
        password_field = self.wait.until(EC.presence_of_element_located(self.key_word))
        move_mouse(self.driver, password_field)
        safe_send(password_field, Password)
        print("password correct")
        print("infos bien remplis")


    def signin_button_click(self):
        wait_random(0.5, 1.1)
        signin_btn = self.wait.until(EC.presence_of_element_located(self.signin_boutton))
        move_mouse(self.driver, signin_btn)
        safeclick_cleanup(self.driver, self.signin_boutton)
        self.driver.save_screenshot("screenshots/after_login.png")
        print("URL actuelle après login :", self.driver.current_url)
        print("✅ Passe à la page d'accueil avec succès")

    

