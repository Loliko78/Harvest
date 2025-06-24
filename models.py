from db import db
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import relationship
import datetime

class User(UserMixin, db.Model):
    id = Column(Integer, primary_key=True)
    nickname_enc = Column(String(64), nullable=False, unique=True)  # Никнейм теперь строка
    password_hash = Column(String(128), nullable=False)
    is_admin = Column(Boolean, default=False)
    banned = Column(Boolean, default=False)
    public_key = Column(LargeBinary, nullable=True)  # Публичный ключ пользователя
    avatar = Column(String(128), nullable=True)  # Путь к аватарке или стандартная иконка
    anonymous_mode = Column(Boolean, default=True)  # Включено ли шифрование
    global_chat_key = Column(String(128), nullable=True)  # Глобальный ключ для чатов
    global_group_key = Column(String(128), nullable=True)  # Глобальный ключ для групп
    chats1 = relationship('Chat', foreign_keys='Chat.user1_id', backref='user1', lazy=True)
    chats2 = relationship('Chat', foreign_keys='Chat.user2_id', backref='user2', lazy=True)

class Chat(db.Model):
    id = Column(Integer, primary_key=True)
    user1_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user2_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    key_enc = Column(LargeBinary, nullable=True)  # E2EE ключ чата
    session_key = Column(LargeBinary, nullable=True)  # Временный ключ сессии для PFS
    session_expires = Column(DateTime, nullable=True)  # Время истечения сессии
    last_read_user1 = Column(DateTime, nullable=True)  # Время последнего прочитанного сообщения для user1
    last_read_user2 = Column(DateTime, nullable=True)  # Время последнего прочитанного сообщения для user2
    messages = relationship('Message', backref='chat', lazy=True)

class Group(db.Model):
    id = Column(Integer, primary_key=True)
    name_enc = Column(LargeBinary, nullable=False)
    invite_link_enc = Column(LargeBinary, nullable=False, unique=True)
    creator_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # Создатель группы
    session_key = Column(LargeBinary, nullable=True)  # Временный ключ сессии для PFS
    session_expires = Column(DateTime, nullable=True)  # Время истечения сессии
    avatar = Column(String(128), nullable=True)  # Путь к аватарке или стандартная иконка
    messages = relationship('Message', backref='group', lazy=True)

class Message(db.Model):
    id = Column(Integer, primary_key=True)
    chat_id = Column(Integer, ForeignKey('chat.id'), nullable=True)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=True)
    sender_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    content_enc = Column(LargeBinary, nullable=False)  # Зашифрованное сообщение
    type = Column(String(16), default='text')  # text, file, audio
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    deleted = Column(Boolean, default=False)
    session_id = Column(String(64), nullable=True)  # ID сессии для PFS
    file = relationship('File', backref='message', uselist=False)

class File(db.Model):
    id = Column(Integer, primary_key=True)
    message_id = Column(Integer, ForeignKey('message.id'), nullable=False)
    filename_enc = Column(LargeBinary, nullable=False)
    path_enc = Column(LargeBinary, nullable=False)
    file_key_enc = Column(LargeBinary, nullable=False)
    type = Column(String(50), nullable=False)

class GroupMember(db.Model):
    id = Column(Integer, primary_key=True)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    last_read = Column(DateTime, nullable=True)  # Время последнего прочитанного сообщения

class ReadTracking(db.Model):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    chat_id = Column(Integer, ForeignKey('chat.id'), nullable=False)
    last_read = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)

class Channel(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    description = Column(String(256), nullable=True)
    creator_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    avatar = Column(String(128), nullable=True)  # Путь к аватарке или стандартная иконка
    key_enc = Column(LargeBinary, nullable=True)
    deleted = Column(db.Boolean, default=False)  # Мягкое удаление канала
    posts = relationship('ChannelPost', backref='channel', lazy='dynamic')

class ChannelPost(db.Model):
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey('channel.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    content = Column(String(2048), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    comments = relationship('ChannelComment', backref='post', lazy='dynamic', cascade='all, delete-orphan')

class ChannelComment(db.Model):
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('channel_post.id'), nullable=False)
    author_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    content = Column(String(1024), nullable=False)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
    author = relationship('User', backref='channel_comments', lazy='joined')

class ChannelSubscriber(db.Model):
    id = Column(Integer, primary_key=True)
    channel_id = Column(Integer, ForeignKey('channel.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

# !!! После добавления avatar и Channel не забудь выполнить миграцию БД (alembic или вручную) !!! 