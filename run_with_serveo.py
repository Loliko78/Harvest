#!/usr/bin/env python3
"""
Запуск Flask с Serveo
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

def start_serveo():
    """Запускает Serveo"""
    try:
        print("🌐 Запуск Serveo...")
        process = subprocess.Popen(
            ['ssh', '-R', '80:localhost:8080', 'serveo.net'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Ловим ссылку из stdout
        url = None
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
            # Ищем ссылку вида https://random-name.serveo.net
            match = re.search(r'https://[\w\-]+\.serveo\.net', line)
            if match and not url:
                url = match.group(0)
                print(f"\n\033[92m🌍 Публичный доступ: {url}\033[0m\n")
                break
            # Также ищем ссылки вида http://random-name.serveo.net
            match = re.search(r'http://[\w\-]+\.serveo\.net', line)
            if match and not url:
                url = match.group(0)
                print(f"\n\033[92m🌍 Публичный доступ: {url}\033[0m\n")
                break
        
        return url, process
        
    except Exception as e:
        print(f"❌ Ошибка запуска Serveo: {e}")
        return None, None

if __name__ == '__main__':
    print("🚀 Запуск Flask с Serveo...")
    print("=" * 50)
    
    # Запускаем Flask
    print("📱 Запуск Flask приложения...")
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Ждем запуска Flask
    time.sleep(3)
    
    # Запускаем Serveo
    public_url, process = start_serveo()
    
    if process:
        if public_url:
            print(f"\n✅ Serveo: {public_url}")
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
            print("\n🛑 Остановка...")
            process.terminate()
            print("✅ Остановлено")
    else:
        print("❌ Не удалось запустить Serveo")
        print("💡 Попробуйте локальный доступ: python run_local.py") 