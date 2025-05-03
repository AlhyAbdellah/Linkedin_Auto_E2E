from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="pages/.env")

Email=os.getenv("LINKEDIN_EMAIL")
Password=os.getenv("LINKEDIN_PASSWORD")
print("EMAIL chargé depuis .env :", Email)
print("passw chargé depuis .env :", Password)
