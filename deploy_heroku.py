#!/usr/bin/env python3
"""
Деплой на Heroku для публичного доступа
"""

import os
import subprocess
import json

def create_heroku_files():
    """Создает файлы для деплоя на Heroku"""
    
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
    
    print("✅ Файлы для Heroku созданы")

def create_deploy_instructions():
    """Создает инструкции по деплою"""
    instructions = """
# 🚀 Деплой на Heroku

## 1. Установите Heroku CLI
Скачайте с: https://devcenter.heroku.com/articles/heroku-cli

## 2. Войдите в Heroku
```bash
heroku login
```

## 3. Создайте приложение
```bash
heroku create harvest-messenger-app
```

## 4. Добавьте базу данных
```bash
heroku addons:create heroku-postgresql:mini
```

## 5. Деплойте приложение
```bash
git add .
git commit -m "Initial commit"
git push heroku main
```

## 6. Откройте приложение
```bash
heroku open
```

## Альтернативный способ через Railway:
1. Перейдите на https://railway.app/
2. Подключите GitHub репозиторий
3. Railway автоматически деплоит приложение
"""
    
    with open('HEROKU_DEPLOY.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Инструкции по деплою созданы")

def create_railway_config():
    """Создает конфигурацию для Railway"""
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
    
    print("✅ Конфигурация Railway создана")

if __name__ == '__main__':
    print("🚀 Подготовка к деплою на Heroku/Railway")
    print("=" * 50)
    
    create_heroku_files()
    create_railway_config()
    create_deploy_instructions()
    
    print("\n✅ Готово!")
    print("💡 Следуйте инструкциям в файле HEROKU_DEPLOY.md")
    print("🌐 Или используйте Railway: https://railway.app/") 