#!/usr/bin/env python3
"""
Установка и настройка PageKite
"""

import subprocess
import sys
import os
import urllib.request
import zipfile

def download_pagekite():
    """Скачивает PageKite"""
    try:
        print("📥 Скачивание PageKite...")
        
        # URL для Windows
        url = "https://pagekite.net/pk/pagekite-win32.zip"
        filename = "pagekite-win32.zip"
        
        # Скачиваем файл
        urllib.request.urlretrieve(url, filename)
        print("✅ PageKite скачан")
        
        # Распаковываем
        with zipfile.ZipFile(filename, 'r') as zip_ref:
            zip_ref.extractall("pagekite")
        
        # Перемещаем exe файл
        os.rename("pagekite/pagekite.exe", "pagekite.exe")
        
        # Удаляем временные файлы
        os.remove(filename)
        import shutil
        shutil.rmtree("pagekite")
        
        print("✅ PageKite установлен")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка скачивания: {e}")
        return False

def create_pagekite_script():
    """Создает скрипт для запуска с PageKite"""
    script_content = '''#!/usr/bin/env python3
"""
Запуск Flask с PageKite
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

def start_pagekite():
    """Запускает PageKite"""
    try:
        print("🌐 Запуск PageKite...")
        process = subprocess.Popen(
            ['pagekite.exe', '8080', 'harvest-messenger.pagekite.me'],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Ждем немного для получения ссылки
        time.sleep(5)
        
        # Проверяем, работает ли процесс
        if process.poll() is None:
            url = "https://harvest-messenger.pagekite.me"
            print(f"\\n\\033[92m🌍 Публичный доступ: {url}\\033[0m\\n")
            return url, process
        else:
            process.terminate()
            return None, None
        
    except Exception as e:
        print(f"❌ Ошибка запуска PageKite: {e}")
        return None, None

if __name__ == '__main__':
    print("🚀 Запуск Flask с PageKite...")
    print("=" * 50)
    
    # Запускаем Flask
    print("📱 Запуск Flask приложения...")
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.daemon = True
    flask_thread.start()
    
    # Ждем запуска Flask
    time.sleep(3)
    
    # Запускаем PageKite
    public_url, process = start_pagekite()
    
    if process:
        if public_url:
            print(f"\\n✅ PageKite: {public_url}")
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
        print("❌ Не удалось запустить PageKite")
        print("💡 Попробуйте локальный доступ: python run_local.py")
'''
    
    with open('run_with_pagekite.py', 'w', encoding='utf-8') as f:
        f.write(script_content)
    
    print("✅ Скрипт run_with_pagekite.py создан")

if __name__ == '__main__':
    print("🚀 Установка PageKite для публичного доступа")
    print("=" * 50)
    
    if download_pagekite():
        create_pagekite_script()
        print("\n✅ Установка завершена!")
        print("💡 Теперь запустите: python run_with_pagekite.py")
    else:
        print("\n❌ Установка не удалась")
        print("💡 Попробуйте другие способы из LAUNCH_GUIDE.md") 