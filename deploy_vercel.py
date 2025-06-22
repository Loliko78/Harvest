#!/usr/bin/env python3
"""
Деплой на Vercel (бесплатно)
"""

import os
import json

def create_vercel_files():
    """Создает файлы для деплоя на Vercel"""
    
    # Создаем vercel.json
    vercel_config = {
        "version": 2,
        "builds": [
            {
                "src": "app.py",
                "use": "@vercel/python"
            }
        ],
        "routes": [
            {
                "src": "/(.*)",
                "dest": "app.py"
            }
        ]
    }
    
    with open('vercel.json', 'w') as f:
        json.dump(vercel_config, f, indent=2)
    
    # Обновляем requirements.txt
    requirements = [
        "Flask==2.3.3",
        "Flask-SQLAlchemy==3.0.5",
        "Flask-SocketIO==5.3.6",
        "python-socketio==5.8.0",
        "cryptography==41.0.4"
    ]
    
    with open('requirements.txt', 'w') as f:
        f.write('\n'.join(requirements))
    
    print("✅ Файлы для Vercel созданы")

def create_vercel_instructions():
    """Создает инструкции по деплою на Vercel"""
    instructions = """
# 🚀 Деплой на Vercel (БЕСПЛАТНО)

## 1. Подготовка
Запустите этот скрипт для создания необходимых файлов:
```bash
python deploy_vercel.py
```

## 2. Создайте GitHub репозиторий
1. Перейдите на https://github.com/
2. Создайте новый репозиторий
3. Загрузите все файлы проекта

## 3. Деплой на Vercel
1. Перейдите на https://vercel.com/
2. Войдите через GitHub
3. Нажмите "New Project"
4. Импортируйте ваш GitHub репозиторий
5. Vercel автоматически определит Python проект
6. Нажмите "Deploy"

## 4. Получите ссылку
После деплоя Vercel даст вам публичную ссылку вида:
https://harvest-messenger.vercel.app

## 5. Настройка базы данных
Для базы данных используйте:
- Supabase (бесплатно): https://supabase.com/
- PlanetScale (бесплатно): https://planetscale.com/
- Neon (бесплатно): https://neon.tech/

## ✅ Преимущества Vercel:
- 🆓 Полностью бесплатно
- 🚀 Мгновенный деплой
- 📊 Аналитика
- 🔄 Автоматические обновления
- 🌍 Глобальный CDN
- ⚡ Очень быстрая загрузка
"""
    
    with open('VERCEL_DEPLOY.md', 'w', encoding='utf-8') as f:
        f.write(instructions)
    
    print("✅ Инструкции по деплою на Vercel созданы")

if __name__ == '__main__':
    print("🚀 Подготовка к деплою на Vercel (БЕСПЛАТНО)")
    print("=" * 50)
    
    create_vercel_files()
    create_vercel_instructions()
    
    print("\n✅ Готово!")
    print("💡 Следуйте инструкциям в файле VERCEL_DEPLOY.md")
    print("🌐 Vercel: https://vercel.com/") 