import os
import sqlite3

from config.settings import DB_PATH, STUDENTS_NAME_AND_TG_DICT


def initialize_db():
    db_exists = os.path.exists(DB_PATH)

    if not db_exists:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS OP_queue (
            id INTEGER PRIMARY KEY,
            student_name TEXT,
            student_tg_id TEXT,
            Lab1 BOOLEAN,
            Lab2 BOOLEAN,
            Lab3 BOOLEAN,
            Lab4 BOOLEAN,
            Lab5 BOOLEAN,
            Lab6 BOOLEAN,
            Lab7 BOOLEAN,
            Lab8 BOOLEAN
        )
        """
        )

        cursor.execute(
            """
        CREATE TABLE IF NOT EXISTS EVM_queue (
            id INTEGER PRIMARY KEY,
            student_name TEXT,
            student_tg_id TEXT,
            Lab1 BOOLEAN,
            Lab2 BOOLEAN,
            Lab3 BOOLEAN,
            Lab4 BOOLEAN,
            Lab5 BOOLEAN,
            Lab6 BOOLEAN,
            Lab7 BOOLEAN,
            Lab8 BOOLEAN,
            Lab9 BOOLEAN,
            Lab10 BOOLEAN
        )
        """
        )

        for i, (student_tg_id, student_name) in enumerate(
            STUDENTS_NAME_AND_TG_DICT.items(), start=1
        ):
            cursor.execute(
                "INSERT INTO OP_queue (id, student_name, student_tg_id, Lab1, Lab2, Lab3, Lab4, Lab5, Lab6, Lab7, Lab8) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    i,
                    student_name,
                    student_tg_id,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ),
            )
            cursor.execute(
                "INSERT INTO EVM_queue (id, student_name, student_tg_id, Lab1, Lab2, Lab3, Lab4, Lab5, Lab6, Lab7, Lab8, Lab9, Lab10) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    i,
                    student_name,
                    student_tg_id,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                    False,
                ),
            )

        conn.commit()
        conn.close()
