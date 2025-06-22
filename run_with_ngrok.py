#!/usr/bin/env python3
"""
Запуск Flask с Ngrok Tunnel
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

def start_ngrok_tunnel():
    """Запускает Ngrok Tunnel"""
    ngrok_path = "./ngrok.exe"
    
    if not os.path.exists(ngrok_path):
        print("❌ Ngrok не найден. Скачайте ngrok.exe и поместите в корневую папку")
        return None, None
    
    try:
        print("🌐 Запуск Ngrok Tunnel...")
        process = subprocess.Popen(
            [ngrok_path, 'http', '8080'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Ловим ссылку из stdout
        url = None
        for line in iter(process.stdout.readline, ''):
            print(line, end='')
            # Ищем ссылку вида https://random-name.ngrok-free.app
            match = re.search(r'https://[\w\-]+\.ngrok-free\.app', line)
            if match and not url:
                url = match.group(0)
                print(f"\n\033[92m🌍 Публичный доступ: {url}\033[0m\n")
                break
            # Также ищем ссылки вида https://random-name.ngrok.io
            match = re.search(r'https://[\w\-]+\.ngrok\.io', line)
            if match and not url:
                url = match.group(0)
                print(f"\n\033[92m🌍 Публичный доступ: {url}\033[0m\n")
                break
        
        return url, process
        
    except Exception as e:
        print(f"❌ Ошибка запуска Ngrok Tunnel: {e}")
        return None, None

if __name__ == '__main__':
    print("🚀 Запуск Flask с Ngrok Tunnel...")
    print("=" * 50)
    
    # Запускаем Flask
    print("📱 Запуск Flask приложения...")
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Ждем запуска Flask
    time.sleep(3)
    
    # Запускаем Ngrok Tunnel
    public_url, process = start_ngrok_tunnel()
    
    if process:
        if public_url:
            print(f"\n✅ Ngrok Tunnel: {public_url}")
            print(f"📱 Локальный доступ: http://127.0.0.1:8080")
            print("=" * 50)
            print("💡 Нажмите Ctrl+C для остановки")
            print("🔒 Без предупреждений и паролей!")
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
        print("❌ Не удалось запустить Ngrok Tunnel")
        print("💡 Попробуйте локальный доступ: python run_local.py") 