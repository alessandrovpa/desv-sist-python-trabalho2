import sqlite3

DB_PATH = '../python-bd/'
DB_NAME = 'database.db'

conn = sqlite3.connect(DB_PATH+DB_NAME)
cursor = conn.cursor()