from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from config.settings import BOT_TOKEN
from bot.handlers.user_side import handlers as user_handlers
from bot.handlers.admin_side import handlers as admin_handlers
from database.db_generating import initialize_db

def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher(bot)
    dp.middleware.setup(LoggingMiddleware())

    initialize_db()

    user_handlers.register_handlers_user(dp)
    admin_handlers.register_handlers_admin(dp)

    executor.start_polling(dp, skip_updates=True)

if __name__ == "__main__":
    main()
