from aiogram.dispatcher.filters.state import State,StatesGroup

class Murojaat(StatesGroup):
    ism_qabul_qilish = State()
    familya_qabul_qilish: State = State()
    yosh_qabul_qilish = State()
    tel_qabul_qilish = State()
    murojaat_qabul_qilish = State()
    tasdiqlash_holati = State()