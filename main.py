from controllers.personController import get, create
from database.person import create_table
import database.database
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *

create_table()

root = Tk()
root.title('Cadastro e consulta de notas')

materia = tk.StringVar()
nota1 = tk.DoubleVar()
nota2 = tk.DoubleVar()

def submitData():
    if materia.get() == "" or nota1.get() == "" or nota2.get() == "":
        resultado = tk.showwarning("", "Preencha todos os campos", icon="warning")
    else:
        create(materia.get(), nota1.get(), nota2.get())
        materia.set("")
        nota1.set("")
        nota2.set("")
        listingPersons()

def listingPersons():
    listView.delete(*listView.get_children())
    persons = get()
    for p in persons:
        listView.insert("", "end", value=[p[1], p[2], p[3], p[4]])

formPerson = Frame(root)
formPerson.pack(side=TOP)

labelMateria = Label(formPerson, text="Materia")
labelMateria.grid(row=0,column=0)
labelNota1 = Label(formPerson, text="Nota 1")
labelNota1.grid(row=1,column=0)
labelNota2 = Label(formPerson, text="Nota 2")
labelNota2.grid(row=2,column=0)

entryMateria = Entry(formPerson, textvariable=materia)
entryMateria.grid(row=0, column=1)
entryNota1 = Entry(formPerson, textvariable=nota1)
entryNota1.grid(row=1, column=1)
entryNota2 = Entry(formPerson, textvariable=nota2)
entryNota2.grid(row=2, column=1)
btnEnviar = Button(formPerson, text="Enviar", width=50, command=submitData)
btnEnviar.grid(row=3, columnspan=2)

listPersons = Frame(root)
labelTitle = Label(listPersons, text="Minhas notas")
labelTitle.grid(row=0, column=0)
listPersons.pack(side=BOTTOM)
listView = ttk.Treeview(listPersons, columns=["materia", "nota1", "nota2", "situacao"], show="headings")
listView.heading('materia', text="Matéria")
listView.heading('nota1', text="Nota 1")
listView.heading('nota2', text="Nota 2")
listView.heading('situacao', text="situacao")

listView.grid(row=1, column=0)
listingPersons()
root.mainloop()