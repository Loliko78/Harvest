#!/usr/bin/env python3
"""
Запуск Flask с доступом через локальную сеть
"""

import socket
import requests
from app import app

def get_local_ip():
    """Получает локальный IP адрес"""
    try:
        # Подключаемся к внешнему серверу, чтобы узнать наш IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except:
        return "127.0.0.1"

def check_port_available(host, port):
    """Проверяет, доступен ли порт"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host, port))
        sock.close()
        return result != 0
    except:
        return False

if __name__ == '__main__':
    print("🚀 Запуск Flask приложения с сетевым доступом...")
    print("=" * 50)
    
    # Получаем локальный IP
    local_ip = get_local_ip()
    port = 5000
    
    # Проверяем доступность порта
    if not check_port_available(local_ip, port):
        print(f"⚠️ Порт {port} занят, пробуем 8080...")
        port = 8080
        if not check_port_available(local_ip, port):
            print(f"⚠️ Порт {port} тоже занят, пробуем 3000...")
            port = 3000
    
    print(f"📱 Локальный доступ: http://127.0.0.1:{port}")
    print(f"🌐 Сетевой доступ: http://{local_ip}:{port}")
    print("=" * 50)
    print("💡 Другие устройства в сети смогут подключиться по сетевому адресу")
    print("💡 Нажмите Ctrl+C для остановки")
    
    try:
        app.run(host='0.0.0.0', port=port, debug=True)
    except KeyboardInterrupt:
        print("\n🛑 Остановка...")
        print("✅ Остановлено") 