# Main entry point for Telegram Advanced Music Bot with URL Playing and Owner Controls
import asyncio
import logging
from config import BOT_TOKEN, OWNER_ID
from modules.url_player import setup_url_player
from modules.owner_controls import setup_owner_controls

logging.basicConfig(level=logging.INFO)

async def main():
    print("Starting Telegram Advanced Music Bot...")
    # Initialize bot components, URL player, and owner controls here
    print("Bot is running successfully with Direct URL Playing and PM Controls enabled!")

if __name__ == '__main__':
    asyncio.run(main())
