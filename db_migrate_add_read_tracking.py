#!/usr/bin/env python3
"""
Миграция для добавления полей отслеживания прочитанных сообщений
"""

import sqlite3
import os

def migrate():
    """Добавляем поля для отслеживания прочитанных сообщений"""
    db_path = 'instance/harvest.db'
    
    if not os.path.exists(db_path):
        print("❌ База данных не найдена")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        # Добавляем поля в таблицу Chat
        cursor.execute("""
            ALTER TABLE chat 
            ADD COLUMN last_read_user1 DATETIME
        """)
        print("✅ Добавлено поле last_read_user1 в таблицу chat")
        
        cursor.execute("""
            ALTER TABLE chat 
            ADD COLUMN last_read_user2 DATETIME
        """)
        print("✅ Добавлено поле last_read_user2 в таблицу chat")
        
        # Добавляем поле в таблицу group_member
        cursor.execute("""
            ALTER TABLE group_member 
            ADD COLUMN last_read DATETIME
        """)
        print("✅ Добавлено поле last_read в таблицу group_member")
        
        conn.commit()
        print("🎯 Миграция завершена успешно!")
        
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e):
            print("⚠️  Поля уже существуют, миграция не требуется")
        else:
            print(f"❌ Ошибка миграции: {e}")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    migrate() 