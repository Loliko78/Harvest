#!/usr/bin/env python3
"""
Универсальный скрипт для запуска с любым доступным туннелем
"""

import threading
import time
import subprocess
import re
import os
import socket
from app import app

def get_local_ip():
    """Получает локальный IP адрес"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

def run_flask():
    """Запускает Flask приложение"""
    app.run(host='127.0.0.1', port=8080, debug=False)

def try_cloudflare():
    """Пробует запустить Cloudflare Tunnel"""
    cloudflared_path = "./cloudflared.exe"
    
    if not os.path.exists(cloudflared_path):
        return None, None
    
    try:
        print("🌐 Пробуем Cloudflare Tunnel...")
        process = subprocess.Popen(
            [cloudflared_path, 'tunnel', '--url', 'http://127.0.0.1:8080'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Ждем немного для получения ссылки
        time.sleep(5)
        
        # Проверяем, работает ли процесс
        if process.poll() is None:
            return "Cloudflare", process
        else:
            process.terminate()
            return None, None
            
    except Exception as e:
        print(f"❌ Cloudflare не работает: {e}")
        return None, None

def try_ngrok():
    """Пробует запустить Ngrok Tunnel"""
    ngrok_path = "./ngrok.exe"
    
    if not os.path.exists(ngrok_path):
        return None, None
    
    try:
        print("🌐 Пробуем Ngrok Tunnel...")
        process = subprocess.Popen(
            [ngrok_path, 'http', '8080'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Ждем немного для получения ссылки
        time.sleep(5)
        
        # Проверяем, работает ли процесс
        if process.poll() is None:
            return "Ngrok", process
        else:
            process.terminate()
            return None, None
            
    except Exception as e:
        print(f"❌ Ngrok не работает: {e}")
        return None, None

def try_localtunnel():
    """Пробует запустить Localtunnel"""
    try:
        print("🌐 Пробуем Localtunnel...")
        process = subprocess.Popen(
            ['lt', '--port', '8080', '--subdomain', 'harvest-messenger'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Ждем немного для получения ссылки
        time.sleep(5)
        
        # Проверяем, работает ли процесс
        if process.poll() is None:
            return "Localtunnel", process
        else:
            process.terminate()
            return None, None
            
    except Exception as e:
        print(f"❌ Localtunnel не работает: {e}")
        return None, None

def try_serveo():
    """Пробует запустить Serveo"""
    try:
        print("🌐 Пробуем Serveo...")
        process = subprocess.Popen(
            ['ssh', '-R', '80:localhost:8080', 'serveo.net'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Ждем немного для получения ссылки
        time.sleep(5)
        
        # Проверяем, работает ли процесс
        if process.poll() is None:
            return "Serveo", process
        else:
            process.terminate()
            return None, None
            
    except Exception as e:
        print(f"❌ Serveo не работает: {e}")
        return None, None

def start_network_mode():
    """Запускает режим сетевого доступа"""
    local_ip = get_local_ip()
    print(f"🌐 Сетевой режим: http://{local_ip}:8080")
    return "Network", None

if __name__ == '__main__':
    print("🚀 Универсальный запуск Flask приложения...")
    print("=" * 50)
    
    # Запускаем Flask
    print("📱 Запуск Flask приложения...")
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Ждем запуска Flask
    time.sleep(3)
    
    # Пробуем разные варианты
    tunnel_name = None
    process = None
    
    # 1. Пробуем Cloudflare
    tunnel_name, process = try_cloudflare()
    
    # 2. Если Cloudflare не работает, пробуем Ngrok
    if not tunnel_name:
        tunnel_name, process = try_ngrok()
    
    # 3. Если Ngrok не работает, пробуем Localtunnel
    if not tunnel_name:
        tunnel_name, process = try_localtunnel()
    
    # 4. Если Localtunnel не работает, пробуем Serveo
    if not tunnel_name:
        tunnel_name, process = try_serveo()
    
    # 5. Если туннели не работают, используем сетевой режим
    if not tunnel_name:
        tunnel_name = start_network_mode()
    
    # Выводим результат
    print("\n" + "=" * 50)
    if tunnel_name == "Network":
        print("✅ Режим: Сетевой доступ")
        print(f"📱 Локальный доступ: http://127.0.0.1:8080")
        print(f"🌐 Сетевой доступ: http://{get_local_ip()}:8080")
        print("💡 Другие устройства в сети смогут подключиться")
    else:
        print(f"✅ Туннель: {tunnel_name}")
        print(f"📱 Локальный доступ: http://127.0.0.1:8080")
        print("💡 Публичная ссылка появится выше в выводе")
    
    print("=" * 50)
    print("💡 Нажмите Ctrl+C для остановки")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Остановка...")
        if process:
            process.terminate()
        print("✅ Остановлено") 