import sqlite3

DB_PATH = 'instance/harvest.db'

conn = sqlite3.connect(DB_PATH)
c = conn.cursor()

# Проверяем, есть ли уже столбец key_enc
c.execute("PRAGMA table_info(chat)")
columns = [row[1] for row in c.fetchall()]
if 'key_enc' not in columns:
    c.execute('ALTER TABLE chat ADD COLUMN key_enc BLOB')
    print('Поле key_enc успешно добавлено в chat.')
else:
    print('Поле key_enc уже существует.')

conn.commit()
conn.close() 