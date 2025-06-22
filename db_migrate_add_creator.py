from app import app, db
from models import Group

with app.app_context():
    # Добавляем поле creator_id в таблицу Group
    # Для существующих групп устанавливаем creator_id = 1 (первый пользователь)
    db.engine.execute('ALTER TABLE "group" ADD COLUMN creator_id INTEGER REFERENCES user(id)')
    
    # Обновляем существующие группы, устанавливая creator_id = 1
    db.engine.execute('UPDATE "group" SET creator_id = 1 WHERE creator_id IS NULL')
    
    # Делаем поле обязательным
    db.engine.execute('ALTER TABLE "group" ALTER COLUMN creator_id SET NOT NULL')
    
    print("Миграция завершена: добавлено поле creator_id в таблицу Group") 