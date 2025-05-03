from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.helps import safeclick_cleanup
from utils.helps import wait_random
from utils.helps import move_mouse

class Profil:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    
    #Locators
    message_bouton=(By.CLASS_NAME,"artdeco-button__text")

    def visibility_click(self):
        wait_random(0.5, 1.5)
        try:
            element = self.wait.until(EC.element_to_be_clickable(self.message_bouton))
            move_mouse(self.driver, element)
            safeclick_cleanup(self.driver, element)
            print("✅ Bouton Message cliqué avec succès")
        except TimeoutException:
            print("❌ Échec : bouton message introuvable ou non cliquable.")
        except Exception as e:
            print("❌ Erreur inattendue dans visibility_click :", e)
