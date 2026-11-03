# Owner PM Control Module
from config import OWNER_ID
import config

async def handle_owner_toggle(client, message):
    if message.from_user.id != OWNER_ID:
        await message.reply("⚠️ You are not authorized to use this command.")
        return
    
    command_parts = message.text.split()
    if len(command_parts) < 2:
        await message.reply("Usage: /toggleurl on or /toggleurl off")
        return
        
    status = command_parts[1].lower()
    if status == "on":
        config.URL_PLAYING_ENABLED = True
        await message.reply("✅ Direct URL playing has been turned ON globally.")
    elif status == "off":
        config.URL_PLAYING_ENABLED = False
        await message.reply("❌ Direct URL playing has been turned OFF globally.")
    else:
        await message.reply("Invalid argument. Use 'on' or 'off'.")
