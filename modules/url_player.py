# Direct URL Playing Module
from config import URL_PLAYING_ENABLED

def is_url_playing_allowed(chat_id):
    # Check if URL based playing is globally or locally enabled
    return URL_PLAYING_ENABLED

async def play_url_from_link(client, message, url):
    if not is_url_playing_allowed(message.chat.id):
        await message.reply("❌ Direct URL playing has been disabled by the bot owner.")
        return
    
    await message.reply(f"🎵 Processing and streaming audio from URL: {url}")
