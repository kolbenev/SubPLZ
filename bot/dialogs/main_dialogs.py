from pathlib import Path

from aiogram_dialog import Window
from aiogram_dialog.widgets.kbd import SwitchTo, Url, Button
from aiogram_dialog.widgets.media import StaticMedia
from aiogram_dialog.widgets.text import Const

from bot.dialogs.utils import check_sub_user
from bot.states import States


main_window = Window(
    StaticMedia(path=Path("media/present.png")),
    Const(
        """
Приветствую тебя на нашем канале! 😀
Нажмите кнопку ниже, чтобы получить доступ к практическому материалу 👇
        """
    ),
    SwitchTo(
        Const("🎁 Получить практический материал"),
        state=States.give_channel,
        id="give_channel",
    ),
    state=States.main_menu
)


sub_or_channel_window = Window(
    StaticMedia(path=Path("media/logo.jpg")),
    Const("Сначала подпишитесь на наш канал, чтобы продолжить 👇"),
    Url(
        text=Const("АлгоРРитм Продаж и HR"),
        url=Const("https://t.me/algorritm_pro"),
    ),
    Button(
        Const("🔄 Готово, я подписался"),
        on_click=check_sub_user,
        id="check_sub",
    ),
    state=States.give_channel,
)