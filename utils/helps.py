from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

#SafeSend
def safe_send(element,value):
    element.clear()
    element.send_keys(value)

#WaitRandom
def wait_random(min_sec, max_sec):
    time.sleep(random.uniform(min_sec,max_sec))

#safeclick_cleanup # Clic avancé : gère iframe, scroll, overlay, JS click
def safeclick_cleanup(driver,element):
    try:
        #baypass l'iframe si present
        driver.switch_to.default_content()# Revenir à la racine au cas où il y a une iframe

        #scroll vers l'element
        driver.execute_script("arguments[0].scrollIntoView({behavior:'smooth', block:'center'});",element)
        wait_random(0.4, 1.1)

        #check element to be clickable
        WebDriverWait(driver,10).until(EC.element_to_be_clickable(element))

        #forcer click via JS
        driver.execute_script("arguments[0].click();",element)# Click JS pour contourner blocages
    except Exception as e:
        print(f"Erreur safe click_cleanup : {e}")


#MouveMouse
def move_mouse(driver,element):
    actions=ActionChains(driver)
    actions.move_to_element(element).perform()
    wait_random(0.4,1.1)


# Gérer les popups si présents (ex: cookies, newsletter)
def close_popup_if_present(driver, popup_selector):
    try:
        popup = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.CSS_SELECTOR, popup_selector)))
        safeclick_cleanup(driver, popup)
    except:
        pass  # Aucun popup n'est apparu

# Scroll infini pour charger plus de contenu dynamiquement
def scroll_to_bottom(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        wait_random(1, 2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

# Recherche + sélection d’un élément dans une liste dynamique
def search_and_select(driver, search_input_locator, keyword, result_selector, target_text):
    search_box = driver.find_element(*search_input_locator)
    search_box.clear()
    search_box.send_keys(keyword)
    wait_random(1, 2)

    results = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, result_selector))
    )

    print("Résultats récupérés :")
    for item in results:
        print("-", item.text.strip())
        if target_text.lower() in item.text.lower():
            safeclick_cleanup(driver, item)
            return
    print("Cible non trouvée dans les résultats de recherche.")

# Upload d'un fichier (champ type='file')
def upload_file(driver, input_selector, file_path):
    upload_input = driver.find_element(By.CSS_SELECTOR, input_selector)
    upload_input.send_keys(file_path)  # Selenium envoie le chemin du fichier

# Gérer les iframes : basculer vers une iframe puis revenir

def switch_to_iframe(driver, iframe_selector):
    iframe = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, iframe_selector))
    )
    driver.switch_to.frame(iframe)

def switch_to_default(driver):
    driver.switch_to.default_content()

# Vérifier la présence d'un élément

def is_element_present(driver, by, locator):
    try:
        driver.find_element(by, locator)
        return True
    except:
        return False

# Mettre en surbrillance un élément (utile en mode debug visuel)
def highlight(driver, element):
    driver.execute_script("arguments[0].style.border='3px solid red'", element)