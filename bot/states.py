from aiogram.fsm.state import StatesGroup, State


class States(StatesGroup):
    main_menu = State()
    give_channel = State()
    give_material = State()