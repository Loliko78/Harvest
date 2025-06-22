#!/usr/bin/env python3
"""
Деплой на Render (бесплатно)
"""

import os
import json

def create_render_files():
    """Создает файлы для деплоя на Render"""
    
    # Создаем Procfile
    procfile_content = "web: gunicorn app:app"
    with open('Procfile', 'w') as f:
        f.write(procfile_content)
    
    # Создаем runtime.txt
    runtime_content = "python-3.9.18"
    with open('runtime.txt', 'w') as f:
        f.write(runtime_content)
    
    # Обновляем requirements.txt
    requirements = [
        "Flask==2.3.3",
        "Flask-SQLAlchemy==3.0.5",
        "Flask-SocketIO==5.3.6",
        "python-socketio==5.8.0",
        "cryptography==41.0.4",
        "gunicorn==21.2.0"
    ]
    
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(requirements))
    
    print("✅ Файлы для Render созданы")

def create_render_instructions():
    """Создает инструкции по деплою на Render"""
    instructions = """
# 🚀 Деплой на Render (БЕСПЛАТНО)

## 1. Подготовка
Запустите этот скрипт для создания необходимых файлов:
```bash
python deploy_render.py
```

## 2. Создайте GitHub репозиторий
1. Перейдите на https://github.com/
2. Создайте новый репозиторий
3. Загрузите все файлы проекта

## 3. Деплой на Render
1. Перейдите на https://render.com/
2. Войдите через GitHub
3. Нажмите "New +"
4. Выберите "Web Service"
5. Подключите ваш GitHub репозиторий
6. Настройте:
   - Name: harvest-messenger
   - Environment: Python 3
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
7. Нажмите "Create Web Service"

## 4. Получите ссылку
После деплоя Render даст вам публичную ссылку вида:
https://harvest-messenger.onrender.com

## 5. Настройка базы данных
1. В Render Dashboard нажмите "New +"
2. Выберите "PostgreSQL"
3. Создайте базу данных
4. Скопируйте переменные окружения в настройки Web Service

## ✅ Преимущества Render:
- 🆓 Полностью бесплатно
- 🚀 Автоматический деплой
- 📊 Мониторинг
- 🔄 Автоматические обновления
- 🌍 Глобальный CDN
- 💾 Бесплатная база данных
"""
    
    with open('RENDER_DEPLOY.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Инструкции по деплою на Render созданы")

if __name__ == '__main__':
    print("🚀 Подготовка к деплою на Render (БЕСПЛАТНО)")
    print("=" * 50)
    
    create_render_files()
    create_render_instructions()
    
    print("\n✅ Готово!")
    print("💡 Следуйте инструкциям в файле RENDER_DEPLOY.md")
    print("🌐 Render: https://render.com/") 