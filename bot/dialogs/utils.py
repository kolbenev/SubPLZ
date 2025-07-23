from aiogram import Bot
from aiogram.types import ChatMember, CallbackQuery, FSInputFile
from aiogram_dialog import DialogManager, ShowMode
from aiogram_dialog.widgets.kbd import Button

from bot.logger import logger
from bot.states import States
from load_env import CHANNEL_ID


async def is_user_subscribed(user_id: int, bot: Bot) -> bool | None:
    try:
        member: ChatMember = await bot.get_chat_member(CHANNEL_ID, user_id)
        return member.status in ("member", "administrator", "creator")
    except Exception as e: pass


async def check_sub_user(
    callback_query: CallbackQuery, button: Button, dialog_manager: DialogManager
):
    result = await is_user_subscribed(
        user_id=callback_query.message.chat.id,
        bot=dialog_manager.event.bot,
    )

    if not result:
        await callback_query.message.answer(
            text="⚠️ Похоже, вы ещё не подписались на канал. Подпишитесь и нажмите «🔄 Готово, я подписался», "
        ),
        await dialog_manager.switch_to(
            state=States.give_channel,
            show_mode=ShowMode.DELETE_AND_SEND,
        )
        logger.info(f"{callback_query.from_user.id}: {callback_query.from_user.username} "
                    f"Не подписался на канал")
        return

    await dialog_manager.done()

    logger.info(f"{callback_query.from_user.id}: {callback_query.from_user.username} "
                f"Подписался на канал и получил ПДФ.")

    pdf = FSInputFile("media/АлгоРРитм_Топ_Техник.pdf")
    await dialog_manager.event.bot.send_document(
        chat_id=callback_query.message.chat.id,
        caption="🎉 Ваш практический материал готов к скачиванию! Успехов в применении!",
        document=pdf,
    )