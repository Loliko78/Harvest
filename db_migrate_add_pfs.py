#!/usr/bin/env python3
"""
Миграция для добавления Perfect Forward Secrecy (PFS)
"""

import sqlite3
import os

def migrate():
    db_path = 'instance/harvest.db'
    
    if not os.path.exists(db_path):
        print("База данных не найдена. Создайте её сначала.")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Добавляем поля для PFS в таблицу chat
        cursor.execute("""
            ALTER TABLE chat 
            ADD COLUMN session_key BLOB
        """)
        print("✓ Добавлено поле session_key в таблицу chat")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Поле session_key уже существует в таблице chat")
        else:
            print(f"Ошибка при добавлении session_key: {e}")
    
    try:
        cursor.execute("""
            ALTER TABLE chat 
            ADD COLUMN session_expires TIMESTAMP
        """)
        print("✓ Добавлено поле session_expires в таблицу chat")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Поле session_expires уже существует в таблице chat")
        else:
            print(f"Ошибка при добавлении session_expires: {e}")
    
    try:
        # Добавляем поля для PFS в таблицу group
        cursor.execute("""
            ALTER TABLE "group" 
            ADD COLUMN session_key BLOB
        """)
        print("✓ Добавлено поле session_key в таблицу group")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Поле session_key уже существует в таблице group")
        else:
            print(f"Ошибка при добавлении session_key: {e}")
    
    try:
        cursor.execute("""
            ALTER TABLE "group" 
            ADD COLUMN session_expires TIMESTAMP
        """)
        print("✓ Добавлено поле session_expires в таблицу group")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Поле session_expires уже существует в таблице group")
        else:
            print(f"Ошибка при добавлении session_expires: {e}")
    
    try:
        # Добавляем поле session_id в таблицу message
        cursor.execute("""
            ALTER TABLE message 
            ADD COLUMN session_id VARCHAR(64)
        """)
        print("✓ Добавлено поле session_id в таблицу message")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Поле session_id уже существует в таблице message")
        else:
            print(f"Ошибка при добавлении session_id: {e}")
    
    try:
        # Добавляем поле file_key_enc в таблицу file
        cursor.execute("""
            ALTER TABLE file 
            ADD COLUMN file_key_enc BLOB
        """)
        print("✓ Добавлено поле file_key_enc в таблицу file")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Поле file_key_enc уже существует в таблице file")
        else:
            print(f"Ошибка при добавлении file_key_enc: {e}")
    
    conn.commit()
    conn.close()
    print("\n✅ Миграция PFS завершена успешно!")

if __name__ == '__main__':
    migrate() 