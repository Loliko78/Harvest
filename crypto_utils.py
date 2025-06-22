from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
from PIL import Image
import piexif
import base64

def generate_aes_key():
    return os.urandom(32)

def encrypt_aes(key, plaintext):
    iv = os.urandom(16)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(plaintext) + padder.finalize()
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ct

def decrypt_aes(key, ciphertext):
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_data = decryptor.update(ct) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    return data

def encrypt_file(file_path, output_path=None):
    """Шифрует файл на сервере"""
    if output_path is None:
        output_path = file_path + '.enc'
    
    # Генерируем ключ для файла
    file_key = generate_aes_key()
    
    # Читаем файл
    with open(file_path, 'rb') as f:
        file_data = f.read()
    
    # Шифруем
    encrypted_data = encrypt_aes(file_key, file_data)
    
    # Сохраняем зашифрованный файл
    with open(output_path, 'wb') as f:
        f.write(encrypted_data)
    
    # Возвращаем ключ для сохранения в БД
    return file_key, output_path

def decrypt_file(file_path, key, output_path=None):
    """Расшифровывает файл"""
    if output_path is None:
        output_path = file_path.replace('.enc', '')
    
    # Читаем зашифрованный файл
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()
    
    # Расшифровываем
    decrypted_data = decrypt_aes(key, encrypted_data)
    
    # Сохраняем расшифрованный файл
    with open(output_path, 'wb') as f:
        f.write(decrypted_data)
    
    return output_path

def hash_password(password):
    from werkzeug.security import generate_password_hash
    return generate_password_hash(password, method='pbkdf2:sha256')

def check_password(hash, password):
    from werkzeug.security import check_password_hash
    return check_password_hash(hash, password)

def remove_exif_and_mark(photo_path, output_path):
    img = Image.open(photo_path)
    img.save(output_path, exif=piexif.dump({"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}))
    # Добавляем надпись HARVEST PHOTO (можно добавить watermark, если нужно)
    # Здесь просто сохраняем без EXIF
    return output_path 