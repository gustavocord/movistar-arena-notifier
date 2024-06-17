import os
import asyncio
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import telegram

# Configuración de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuración
TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHANNEL_USERNAME = os.getenv('TELEGRAM_CHANNEL_USERNAME')
SHOW_URL = os.getenv('SHOW_URL')


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

def get_driver():
    """Inicializa el driver de Selenium con las opciones configuradas."""
    return webdriver.Chrome(options=chrome_options)

async def send_message_to_channel(message):
    """Envía un mensaje a un canal de Telegram."""
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    await bot.send_message(chat_id=TELEGRAM_CHANNEL_USERNAME, text=message)
    logger.info(f"Mensaje enviado al canal de Telegram: '{message}'")

def check_button_exists(driver):
    """Verifica si el botón 'Comprar' está presente en la página."""
    try:
        driver.get(SHOW_URL)
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "main-evento-ficha"))
        )
        html_after_interaction = driver.page_source
        soup = BeautifulSoup(html_after_interaction, 'html.parser')
        button_message = soup.find_all('span', class_='mud-button-label')
        button_exists = any(button.text == 'Comprar' for button in button_message)
        logger.info(f"Estado del botón 'Comprar': {'Encontrado' if button_exists else 'No encontrado'}")
        return button_exists
    except Exception as e:
        logger.error(f"Error al verificar el botón: {e}")
        return False

async def main():
    if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHANNEL_USERNAME:
        logger.error("Las variables de entorno TELEGRAM_BOT_TOKEN y TELEGRAM_CHANNEL_USERNAME son necesarias")
        return
    
    driver = get_driver()
    
    try:
        if check_button_exists(driver):
            notification_message = "¡Hay entradas para Keane!"
            await send_message_to_channel(notification_message)
    
    finally:
        driver.quit()

if __name__ == "__main__":
    asyncio.run(main())
