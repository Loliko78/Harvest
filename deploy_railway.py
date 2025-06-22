#!/usr/bin/env python3
"""
Деплой на Railway (бесплатно)
"""

import os
import json

def create_railway_files():
    """Создает файлы для деплоя на Railway"""
    
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
    
    # Создаем railway.json
    railway_config = {
        "build": {
            "builder": "nixpacks"
        },
        "deploy": {
            "startCommand": "gunicorn app:app",
            "healthcheckPath": "/",
            "healthcheckTimeout": 300,
            "restartPolicyType": "ON_FAILURE",
            "restartPolicyMaxRetries": 10
        }
    }
    
    with open('railway.json', 'w') as f:
        json.dump(railway_config, f, indent=2)
    
    print("✅ Файлы для Railway созданы")

def create_railway_instructions():
    """Создает инструкции по деплою на Railway"""
    instructions = """
# 🚀 Деплой на Railway (БЕСПЛАТНО)

## 1. Подготовка
Запустите этот скрипт для создания необходимых файлов:
```bash
python deploy_railway.py
```

## 2. Создайте GitHub репозиторий
1. Перейдите на https://github.com/
2. Создайте новый репозиторий
3. Загрузите все файлы проекта

## 3. Деплой на Railway
1. Перейдите на https://railway.app/
2. Войдите через GitHub
3. Нажмите "New Project"
4. Выберите "Deploy from GitHub repo"
5. Выберите ваш репозиторий
6. Railway автоматически деплоит приложение

## 4. Получите ссылку
После деплоя Railway даст вам публичную ссылку вида:
https://your-app-name.railway.app

## 5. Настройка базы данных
Railway автоматически создаст PostgreSQL базу данных.

## ✅ Преимущества Railway:
- 🆓 Полностью бесплатно
- 🚀 Автоматический деплой
- 📊 Мониторинг
- 🔄 Автоматические обновления
- 🌍 Глобальный CDN
"""
    
    with open('RAILWAY_DEPLOY.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Инструкции по деплою на Railway созданы")

if __name__ == '__main__':
    print("🚀 Подготовка к деплою на Railway (БЕСПЛАТНО)")
    print("=" * 50)
    
    create_railway_files()
    create_railway_instructions()
    
    print("\n✅ Готово!")
    print("💡 Следуйте инструкциям в файле RAILWAY_DEPLOY.md")
    print("🌐 Railway: https://railway.app/") 