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

    def fill_message_send(self, value):
        try:
            wait_random(0.1, 2)
            message = self.wait.until(EC.presence_of_element_located(self.champ_message))
            move_mouse(self.driver, message)
            print("Contenu saisi dans le champ de message :", value)
            safe_send(message, value)
            self.driver.save_screenshot("debug_message_rempli.png")
            print("✅ Message rédigé via LinkedIn")

            wait_random(0.1, 2)
            eny = self.wait.until(EC.presence_of_element_located(self.envoyer))
            move_mouse(self.driver, eny)
            self.driver.save_screenshot("avant_click_envoyer.png")
            safeclick_cleanup(self.driver, self.envoyer)
            print("✅ Message envoyé via LinkedIn")

            wait_random(0.1, 2)

        except TimeoutException:
            print("❌ Timeout : champ de message ou bouton envoyer non trouvé.")
        except Exception as e:
            print(f"❌ Erreur inattendue lors de l’envoi du message : {e}")

