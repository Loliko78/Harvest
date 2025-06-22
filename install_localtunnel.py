#!/usr/bin/env python3
"""
Установка и настройка Localtunnel
"""

import subprocess
import sys
import os

def install_localtunnel():
    """Устанавливает Localtunnel через npm"""
    try:
        print("📦 Установка Localtunnel...")
        
        # Проверяем, установлен ли Node.js
        try:
            subprocess.run(['node', '--version'], check=True, capture_output=True)
            print("✅ Node.js найден")
        except:
            print("❌ Node.js не найден!")
            print("💡 Скачайте Node.js с https://nodejs.org/")
            return False
        
        # Устанавливаем Localtunnel
        print("📥 Установка Localtunnel...")
        result = subprocess.run(['npm', 'install', '-g', 'localtunnel'], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Localtunnel установлен успешно!")
            return True
        else:
            print(f"❌ Ошибка установки: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def create_localtunnel_script():
    """Создает скрипт для запуска с Localtunnel"""
    script_content = '''#!/usr/bin/env python3
"""
Запуск Flask с Localtunnel
"""

import threading
import time
import subprocess
import re
import os
from app import app

def run_flask():
    """Запускает Flask приложение"""
    app.run(host='127.0.0.1', port=8080, debug=False)

def start_localtunnel():
    """Запускает Localtunnel"""
    try:
        print("🌐 Запуск Localtunnel...")
        process = subprocess.Popen(
            ['lt', '--port', '8080', '--subdomain', 'harvest-messenger'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Ловим ссылку из stdout
        url = None
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
            # Ищем ссылку вида https://harvest-messenger.loca.lt
            match = re.search(r'https://[\w\-]+\.loca\.lt', line)
            if match and not url:
                url = match.group(0)
                print(f"\\n\\033[92m🌍 Публичный доступ: {url}\\033[0m\\n")
                break
        
        return url, process
        
    except Exception as e:
        print(f"❌ Ошибка запуска Localtunnel: {e}")
        return None, None

if __name__ == '__main__':
    print("🚀 Запуск Flask с Localtunnel...")
    print("=" * 50)
    
    # Запускаем Flask
    print("📱 Запуск Flask приложения...")
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Ждем запуска Flask
    time.sleep(3)
    
    # Запускаем Localtunnel
    public_url, process = start_localtunnel()
    
    if process:
        if public_url:
            print(f"\\n✅ Localtunnel: {public_url}")
            print(f"📱 Локальный доступ: http://127.0.0.1:8080")
            print("=" * 50)
            print("💡 Нажмите Ctrl+C для остановки")
        else:
            print("⚠️ Туннель запущен, но ссылка не найдена")
            print("💡 Проверьте вывод выше для ссылки")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("\\n🛑 Остановка...")
            process.terminate()
            print("✅ Остановлено")
    else:
        print("❌ Не удалось запустить Localtunnel")
        print("💡 Попробуйте локальный доступ: python run_local.py")
'''
    
    with open('run_with_localtunnel.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print("✅ Скрипт run_with_localtunnel.py создан")

if __name__ == '__main__':
    print("🚀 Установка Localtunnel для публичного доступа")
    print("=" * 50)
    
    if install_localtunnel():
        create_localtunnel_script()
        print("\n✅ Установка завершена!")
        print("💡 Теперь запустите: python run_with_localtunnel.py")
    else:
        print("\n❌ Установка не удалась")
        print("💡 Попробуйте другие способы из LAUNCH_GUIDE.md") 