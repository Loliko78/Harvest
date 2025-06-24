#!/usr/bin/env python3
"""
Скрипт для локального запуска Flask приложения
"""

from app import app

if __name__ == '__main__':
    print("🚀 Запуск Flask приложения локально...")
    print("📱 Локальный доступ: http://0.0.0.0:5000")
    print("💡 Нажмите Ctrl+C для остановки")
    
    app.run(host='0.0.0.0', port=5000, debug=False) 