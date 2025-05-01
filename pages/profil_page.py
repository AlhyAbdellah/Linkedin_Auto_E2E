from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.helps import safeclick_cleanup


class Profil:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    
    #Locators
    message_bouton=(By.CLASS_NAME,"artdeco-button__text")

    def visibility_click(self,element):
        element = self.wait.until(EC.visibility_of_element_located(self.message_bouton))
        safeclick_cleanup(self.driver,element)
        print("✅ Bouton Message cliqué avec succès")
