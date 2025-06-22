#!/usr/bin/env python3
"""
Генерация правильных 32-байтных ключей для синхронизации
"""

import base64

# Создаем 32-байтные ключи из повторяющихся строк
keys_data = [
    "testkeytestkeytestkeytestkeytestkey",  # 30 символов + дополнение
    "secretkeysecretkeysecretkeysecretkey",  # 30 символов + дополнение
    "anonymouskeyanonymouskeyanonymouskey",  # 30 символов + дополнение
    "darknetkeydarknetkeydarknetkeydarknet",  # 30 символов + дополнение
    "hackerkeyhackerkeyhackerkeyhackerkey",  # 30 символов + дополнение
    "privacykeyprivacykeyprivacykeyprivacy",  # 30 символов + дополнение
    "encryptionkeyencryptionkeyencryption",  # 30 символов + дополнение
    "securitykeysecuritykeysecuritykeysecur",  # 30 символов + дополнение
    "torkeytorkeytorkeytorkeytorkeytorkey",  # 30 символов + дополнение
    "signalkeysignalkeysignalkeysignalkey"   # 30 символов + дополнение
]

print("🔧 Генерация правильных 32-байтных ключей...")
print()

for i, key_data in enumerate(keys_data, 1):
    # Дополняем до 32 байт
    if len(key_data) < 32:
        key_data = key_data.ljust(32, '0')  # Дополняем нулями
    elif len(key_data) > 32:
        key_data = key_data[:32]  # Обрезаем до 32 символов
    
    # Кодируем в base64
    key_b64 = base64.b64encode(key_data.encode('utf-8')).decode('utf-8')
    
    print(f"Ключ {i}: {key_b64}")
    print(f"Длина: {len(key_data)} символов, {len(base64.b64decode(key_b64))} байт")
    print()

print("✅ Все ключи имеют правильную длину 32 байта!") 