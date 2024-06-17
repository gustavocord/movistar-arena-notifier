# Notificador de Entradas para movistar arena

Este script Python utiliza Selenium para monitorear la disponibilidad de entradas para un evento específico en el Movistar Arena y envía notificaciones a un canal de Telegram cuando se encuentran disponibles.

## Requisitos

- Python 3.x
- Bibliotecas Python:
  - `selenium`
  - `beautifulsoup4`
  - `python-telegram-bot`
  - `asyncio`

## Configuración

1. **Variables de Entorno:**
   Asegúrate de tener las siguientes variables de entorno configuradas:

   - `TELEGRAM_BOT_TOKEN`: Token de acceso para tu bot de Telegram (el bot debe ser administrador y tener habilitado el envio de mensajes al canal de telegram).
   - `TELEGRAM_CHANNEL_USERNAME`: Nombre de usuario del canal de Telegram donde se enviarán las notificaciones.
   - `SHOW_URL`: URL del evento en el Movistar Arena..
   - `Telegram API` (python-telegram-bot)

2. **Instalación de Dependencias:**
   ```bash
   pip install -r requirement
