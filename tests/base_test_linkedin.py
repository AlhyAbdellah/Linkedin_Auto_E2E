import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import random
from dotenv import load_dotenv
from pages.home_page import HomePage
from pages.login_page import Loginpage
from pages.acceuil_page import AcceuiPage
from pages.profil_page import Profil
from pages.message_page import Message
from pages.logout_page import Logout


# ---------------------------- FIXTURE SETUP ---------------------------- #
@pytest.fixture(scope="function")
def driver(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# ---------------------------- TEST E2E LINKEDIN ---------------------------- #
def test_linkedin_e2e(driver):
    driver.get("https://www.linkedin.com")
    assert "LinkedIn" in driver.title

    home = HomePage(driver)
    home.visible_Signin_click()
    assert home is not None

    login = Loginpage(driver)
    login.full_email_key_work()
    login.signin_button_click()
    assert login is not None

    acceuil = AcceuiPage(driver)
    acceuil.rechercher_personne("btissam", "btissam moutaouakkil")
    assert acceuil is not None

    profil = Profil(driver)
    profil.visibility_click()
    assert profil is not None

    message = Message(driver)
    message.fill_message_send("Hbiba dyali, Tanmout fik")
    driver.save_screenshot("screenshots/message_envoye.png")
    assert message is not None

    logout = Logout(driver)
    logout.logout()
    assert logout is not None
    driver.save_screenshot("screenshots/message_envoye.png")


# ---------------------------- PYTEST HTML HOOKS ---------------------------- #
def pytest_configure(config):
    config._metadata['Projet'] = 'LinkedIn Automation'
    config._metadata['Testé par'] = 'Ibtissam'
    config.option.htmlpath = 'report_linkedin.html'

def pytest_html_report_title(report):
    report.title = "Rapport de test LinkedIn - E2E"

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = getattr(item.cls, "driver", None)
        if driver:
            screenshot_dir = "screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}_{int(time.time())}.png")
            driver.save_screenshot(screenshot_path)
            if hasattr(item.config, "_html"):
                extra = getattr(rep, "extra", [])
                import pytest_html
                extra.append(pytest_html.extras.image(screenshot_path))
                rep.extra = extra
