import sqlite3

from aiogram import types
from aiogram.types import InputFile

from bot.keyboards import (admin_panel_keyboard, labs_keyboard,
                           subjects_keyboard)
from config.settings import ADMIN_USERS, DB_PATH, LABS_COUNT


def mark_lab_as_done(student_id, subject, lab_number):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    table = f"{subject}_queue"
    query = f"UPDATE {table} SET Lab{lab_number} = 'True' WHERE student_tg_id = ?"
    cursor.execute(query, (student_id,))
    conn.commit()
    conn.close()


async def on_admin_panel(call: types.CallbackQuery):
    user_id = call.from_user.username
    if user_id in ADMIN_USERS:
        await call.message.answer(
            "Вы в админской панели", reply_markup=admin_panel_keyboard()
        )
    else:
        await call.answer("У вас нет доступа к админской панели", show_alert=True)


async def on_edit_student(call: types.CallbackQuery):
    student_id = call.data.split("_")[1]
    await call.message.answer(
        "Выберите предмет для добавления:", reply_markup=subjects_keyboard(student_id)
    )


async def on_subject_selected(call: types.CallbackQuery):
    _, student_id, subject = call.data.split("_")
    await call.message.answer(
        "Выберите лабораторную работу для добавления:",
        reply_markup=labs_keyboard(student_id, subject, LABS_COUNT[subject]),
    )


async def on_lab_selected(call: types.CallbackQuery):
    _, student_id, subject, lab_number = call.data.split("_")
    mark_lab_as_done(student_id, subject, int(lab_number))
    await call.answer(
        f"Лабораторная работа {lab_number} по предмету {subject} отмечена как сданная",
        show_alert=True,
    )


async def handle_get_db(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    username = callback_query.from_user.username

    if username in ADMIN_USERS or str(user_id) in ADMIN_USERS:
        db_file = InputFile(DB_PATH)
        await callback_query.message.answer_document(db_file)
    else:
        await callback_query.answer("У вас нет доступа к этой команде", show_alert=True)


def register_handlers_admin(dp):
    dp.register_callback_query_handler(
        on_admin_panel, lambda call: call.data == "admin_configuration"
    )
    dp.register_callback_query_handler(
        on_edit_student, lambda call: call.data.startswith("edit_")
    )
    dp.register_callback_query_handler(
        on_subject_selected, lambda call: call.data.startswith("subject_")
    )
    dp.register_callback_query_handler(
        on_lab_selected, lambda call: call.data.startswith("lab_")
    )
    dp.register_callback_query_handler(handle_get_db, lambda c: c.data == "get_db")
