from aiogram import Dispatcher, types
import sqlite3
import random
from bot.keyboards import start_keyboard, choose_subject_keyboard, subjects_keyboard, labs_keyboard, admin_panel_keyboard
from config.settings import LABS_COUNT, ADMIN_USERS, DB_PATH

def generate_queue(subject):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    if subject == "OP":
        table = "OP_queue"
        labs = 8
    elif subject == "EVM":
        table = "EVM_queue"
        labs = 10
    else:
        return None

    lab_columns = ' + '.join([f"CASE WHEN Lab{i} = 'True' THEN 1 ELSE 0 END" for i in range(1, labs + 1)])
    query = f"""
    SELECT student_name, student_tg_id, {lab_columns} AS solved_labs
    FROM {table}
    ORDER BY solved_labs DESC, random()
    """

    cursor.execute(query)
    students = cursor.fetchall()
    students.sort(key=lambda x: (-x[2], random.random()))
    conn.close()
    return students

def mark_lab_as_done(student_id, subject, lab_number):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    table = f"{subject}_queue"
    query = f"UPDATE {table} SET Lab{lab_number} = 'True' WHERE student_tg_id = ?"
    cursor.execute(query, (student_id,))
    conn.commit()
    conn.close()

async def start_with_command(message: types.Message):
    message_text = "Привет, группа M3112! Я бот, сделанный для студентов ИСа из группы M3112, который будет составлять порядок сдачи разных работ по разным предметам!"
    await message.reply(message_text, reply_markup=start_keyboard())

async def on_normal_defense_callback(call: types.CallbackQuery):
    message_text = "Выберите предмет для которого хотите сгенерировать очередь:"
    await call.message.answer(message_text, reply_markup=choose_subject_keyboard())

async def on_queue_selection(call: types.CallbackQuery):
    subject = call.data.split('_')[0]
    queue = generate_queue(subject)
    message_text = f"Очередь для предмета {subject}:\n\n"
    message_text += "\n".join([f"{i+1}. {student[0]} - Сдано лабораторных: {student[2]}" for i, student in enumerate(queue)])
    await call.message.answer(message_text)

async def back_to_start(call: types.CallbackQuery):
    await start_with_command(call.message)

def register_handlers_user(dp: Dispatcher):
    dp.register_message_handler(start_with_command, commands=['start'])
    dp.register_callback_query_handler(on_normal_defense_callback, lambda call: call.data == 'choose_subject')
    dp.register_callback_query_handler(on_queue_selection, lambda call: call.data in ['OP_queue', 'EVM_queue'])
    dp.register_callback_query_handler(back_to_start, lambda call: call.data == 'start')
