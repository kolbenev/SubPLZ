from aiogram import Dispatcher, Bot, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, CommandObject, ExceptionTypeFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, ErrorEvent, CallbackQuery
from aiogram_dialog import DialogManager, StartMode, setup_dialogs
from aiogram_dialog.api.exceptions import UnknownIntent

from bot.dialogs import dialog
from bot.logger import logger
from bot.states import States
from load_env import BOT_TOKEN


bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
setup_dialogs(dp)


@dp.message(CommandStart())
async def start(
    message: Message,
    state: FSMContext,
    dialog_manager: DialogManager,
    command: CommandObject,
):
    logger.info(f"{message.from_user.id}:{message.from_user.username} "
                f"Ввел команду /start")
    await dialog_manager.start(
        state=States.main_menu,
        mode=StartMode.RESET_STACK,
    )


@dp.errors(
    ExceptionTypeFilter(UnknownIntent),
    F.update.callback_query.as_("callback_query"),
)
async def unknown_intent_handler(
    event: ErrorEvent,
    callback_query: CallbackQuery,
):
    await callback_query.message.answer(
        text="⚠️ Произошла ошибка! Введите команду: /start."
    )

    return True


async def start_bot():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(dialog)
    logger.info("Бот запущен")
    await dp.start_polling(bot)
