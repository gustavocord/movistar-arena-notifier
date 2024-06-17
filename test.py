from telegram import Bot
import asyncio


# Reemplaza 'YOUR_BOT_TOKEN' con el token de tu bot
bot_token = '6929713863:AAEC0ra-MAWc82UxFn_wZzgUGOXoVDodEPk'
bot = Bot(token=bot_token)

# Reemplaza 'CHANNEL_NAME' con el nombre de tu canal
channel_name = '-1002227900016'

async def send_message(bot, channel_name):
    try:
        # Intenta enviar un mensaje al canal
        await bot.send_message(chat_id=channel_name, text='¡Hola, canal!')
        print('Mensaje enviado exitosamente.')
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Ejecuta la función send_message dentro de un event loop
if __name__ == '__main__':
    asyncio.run(send_message(bot, channel_name))