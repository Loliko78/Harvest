#!/usr/bin/env python3
"""
Скрипт для локального запуска Flask приложения
"""

from app import app

if __name__ == '__main__':
    print("🚀 Запуск Flask приложения локально...")
    print("📱 Локальный доступ: http://127.0.0.1:5000")
    print("💡 Нажмите Ctrl+C для остановки")
    
    app.run(host='127.0.0.1', port=5000, debug=True) 