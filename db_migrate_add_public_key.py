#!/usr/bin/env python3
"""
Миграция для добавления поля public_key в таблицу user
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
        # Добавляем поле public_key в таблицу user
        cursor.execute("""
            ALTER TABLE user 
            ADD COLUMN public_key BLOB
        """)
        print("✓ Добавлено поле public_key в таблицу user")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("Поле public_key уже существует в таблице user")
        else:
            print(f"Ошибка при добавлении public_key: {e}")
    
    conn.commit()
    conn.close()
    print("\n✅ Миграция public_key завершена успешно!")

if __name__ == '__main__':
    migrate() 