from aiogram_dialog import Dialog

from bot.dialogs.main_dialogs import main_window, sub_or_channel_window

dialog = Dialog(
    main_window,
    sub_or_channel_window,
)
