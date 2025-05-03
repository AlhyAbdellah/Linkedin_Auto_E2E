from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Email, Password
from utils.helps import safe_send
from utils.helps import safeclick_cleanup
from utils.helps import wait_random
from utils.helps import move_mouse


class Logout:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    profil_menu = (By.CSS_SELECTOR, "img.global-nav__me-photo")  # l'avatar
    logout_btn = (By.XPATH, "//button[contains(., 'Déconnexion')]")

    def logout(self):
        try:
            wait_random(0.5, 1.1)
            profil = self.wait.until(EC.presence_of_element_located(self.profil_menu))
            move_mouse(self.driver, profil)
            safeclick_cleanup(self.driver, self.profil_menu)
            print("menu sélectionné")

            wait_random(0.5, 1.1)
            logout = self.wait.until(EC.presence_of_element_located(self.logout_btn))
            move_mouse(self.driver, logout)
            safeclick_cleanup(self.driver, self.logout_btn)
            print("🚪 Déconnexion réussie")
        except TimeoutException:
            print("❌ Déconnexion impossible : le menu utilisateur n'a pas été trouvé.")
