from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.helps import search_and_select
from utils.helps import close_popup_if_present
from utils.helps import wait_random
from utils.helps import move_mouse


class AcceuiPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Locators (instance attributes)
        self.search_input_locator = (By.XPATH, "//input[@placeholder='Rechercher']")
        self.result_selector = ".reusable-search__result-container"

    # Méthodes
    def rechercher_personne(self, mot_cle, nom_complet):
        wait_random(0.5, 1.1)
        try:
            champ_recherche = self.wait.until(
                EC.presence_of_element_located(self.search_input_locator)
            )
            print("Champ de recherche détecté :", champ_recherche)
            move_mouse(self.driver, champ_recherche)

            search_and_select(
                self.driver,
                self.search_input_locator,
                mot_cle,
                self.result_selector,
                nom_complet
            )

            print("Page LinkedIn Bien Chargée")

        except TimeoutException:
            print("Erreur : champ de recherche introuvable.")

        except Exception as e:
            print("Erreur inattendue :", e)


