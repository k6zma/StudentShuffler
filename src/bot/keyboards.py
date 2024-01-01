from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config.settings import STUDENTS_NAME_AND_TG_DICT, LABS_COUNT

def start_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="Генерация очереди", callback_data="choose_subject"))
    keyboard.add(InlineKeyboardButton(text="Админская панель", callback_data="admin_configuration"))
    keyboard.add(InlineKeyboardButton(text="Получить копию базы данных", callback_data="get_db"))
    return keyboard

def choose_subject_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(InlineKeyboardButton(text="ОП", callback_data="OP_queue"))
    keyboard.add(InlineKeyboardButton(text="ЭВМ", callback_data="EVM_queue"))
    keyboard.add(InlineKeyboardButton(text="Назад на главную", callback_data="start"))
    return keyboard

def admin_panel_keyboard():
    keyboard = InlineKeyboardMarkup()
    for student_id, student_name in STUDENTS_NAME_AND_TG_DICT.items():
        keyboard.add(InlineKeyboardButton(text=student_name, callback_data=f"edit_{student_id}"))
    keyboard.add(InlineKeyboardButton(text="Назад на главную", callback_data="start"))
    return keyboard

def subjects_keyboard(student_id):
    keyboard = InlineKeyboardMarkup()
    for subject in LABS_COUNT.keys():
        keyboard.add(InlineKeyboardButton(text=subject, callback_data=f"subject_{student_id}_{subject}"))
    keyboard.add(InlineKeyboardButton(text="Назад к админ. панели", callback_data="admin_configuration"))
    return keyboard

def labs_keyboard(student_id, subject, labs_count):
    keyboard = InlineKeyboardMarkup()
    for i in range(1, labs_count + 1):
        keyboard.add(InlineKeyboardButton(text=f"Лабораторная {i}", callback_data=f"lab_{student_id}_{subject}_{i}"))
    keyboard.add(InlineKeyboardButton(text="Назад к выбору предмета", callback_data=f"edit_{student_id}"))
    return keyboard
