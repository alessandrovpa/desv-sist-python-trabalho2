import sqlite3
from database.database import conn
from tkinter import messagebox as mb

def create_table():
    conn.execute("""CREATE TABLE IF NOT EXISTS person(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        materia VARCHAR(255) NOT NULL,
        nota1 REAL NOT NULL,
        nota2 REAL NOT NULL,
        situacao VARCHAR(20) NOT NULL)""")

def create_person(person):
    try:
        conn.execute("INSERT INTO person(materia, nota1, nota2, situacao) VALUES(?,?,?,?)", (person))
        conn.commit()
    except sqlite3.Error as error:
        print(person)
        mb.showerror("Erro", "Error ao criar registro, tente novamente")
        print(error)

def list_persons():
    try:
        persons = conn.execute("SELECT * FROM person")
        
        return persons
    except sqlite3.Error as error:
        print('Falha na consulta: ',error)