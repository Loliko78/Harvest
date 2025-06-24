from db import db
from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey, DateTime

def upgrade():
    # Добавить поле avatar в User
    db.session.execute('ALTER TABLE user ADD COLUMN avatar VARCHAR(128)')
    # Добавить поле avatar в Group
    db.session.execute('ALTER TABLE "group" ADD COLUMN avatar VARCHAR(128)')
    # Создать таблицу Channel
    db.session.execute('''
        CREATE TABLE IF NOT EXISTS channel (
            id INTEGER PRIMARY KEY,
            name VARCHAR(64) NOT NULL,
            description VARCHAR(256),
            creator_id INTEGER NOT NULL,
            avatar VARCHAR(128),
            key_enc BLOB,
            FOREIGN KEY(creator_id) REFERENCES user(id)
        )
    ''')
    # Новые поля для профиля
    db.session.execute('ALTER TABLE user ADD COLUMN anonymous_mode BOOLEAN DEFAULT 1')
    db.session.execute('ALTER TABLE user ADD COLUMN global_chat_key VARCHAR(128)')
    db.session.execute('ALTER TABLE user ADD COLUMN global_group_key VARCHAR(128)')
    # Таблицы для постов, комментариев и подписчиков каналов
    db.session.execute('''
        CREATE TABLE IF NOT EXISTS channel_post (
            id INTEGER PRIMARY KEY,
            channel_id INTEGER NOT NULL,
            author_id INTEGER NOT NULL,
            content VARCHAR(2048) NOT NULL,
            timestamp DATETIME,
            FOREIGN KEY(channel_id) REFERENCES channel(id),
            FOREIGN KEY(author_id) REFERENCES user(id)
        )
    ''')
    db.session.execute('''
        CREATE TABLE IF NOT EXISTS channel_comment (
            id INTEGER PRIMARY KEY,
            post_id INTEGER NOT NULL,
            author_id INTEGER NOT NULL,
            content VARCHAR(1024) NOT NULL,
            timestamp DATETIME,
            FOREIGN KEY(post_id) REFERENCES channel_post(id),
            FOREIGN KEY(author_id) REFERENCES user(id)
        )
    ''')
    db.session.execute('''
        CREATE TABLE IF NOT EXISTS channel_subscriber (
            id INTEGER PRIMARY KEY,
            channel_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            FOREIGN KEY(channel_id) REFERENCES channel(id),
            FOREIGN KEY(user_id) REFERENCES user(id)
        )
    ''')
    db.session.execute('ALTER TABLE channel ADD COLUMN deleted BOOLEAN DEFAULT 0')
    db.session.commit()

def downgrade():
    # Откатить изменения (SQLite не поддерживает DROP COLUMN, только пересоздание таблицы)
    pass 