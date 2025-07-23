import asyncio

from bot.bot_main import start_bot
from bot.logger import logger

if __name__ == '__main__':
    logger.info("Запускаем бота")
    asyncio.run(start_bot())