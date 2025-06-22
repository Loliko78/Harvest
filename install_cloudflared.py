#!/usr/bin/env python3
"""
Автоматическая установка Cloudflare Tunnel (cloudflared)
"""

import os
import subprocess
import sys
import zipfile
import requests
from pathlib import Path

def download_cloudflared():
    """Скачивает cloudflared для Windows"""
    print("📥 Скачивание cloudflared...")
    
    # URL для Windows AMD64
    url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-windows-amd64.exe"
    
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        
        # Сохраняем файл
        exe_path = "cloudflared.exe"
        with open(exe_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print("✅ Cloudflared скачан")
        return exe_path
    except Exception as e:
        print(f"❌ Ошибка скачивания: {e}")
        return None

def test_cloudflared():
    """Тестирует cloudflared"""
    print("🧪 Тестирование cloudflared...")
    
    try:
        cloudflared_path = "./cloudflared.exe"
        result = subprocess.run([cloudflared_path, 'version'], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Cloudflared работает!")
            return True
        else:
            print(f"❌ Ошибка тестирования: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

def main():
    print("🚀 Установка Cloudflare Tunnel для Harvest Messenger")
    print("=" * 60)
    
    # Проверяем, установлен ли уже cloudflared
    if os.path.exists("./cloudflared.exe"):
        print("✅ Cloudflared уже установлен")
        if test_cloudflared():
            print("🎉 Cloudflared готов к использованию!")
            return True
        else:
            print("❌ Проблема с cloudflared")
            return False
    
    # Скачиваем cloudflared
    exe_path = download_cloudflared()
    if not exe_path:
        return False
    
    # Тестируем
    if not test_cloudflared():
        return False
    
    print("\n🎉 Cloudflared успешно установлен!")
    print("💡 Теперь можно запускать: python run_with_cloudflare.py")
    return True

if __name__ == '__main__':
    main() 