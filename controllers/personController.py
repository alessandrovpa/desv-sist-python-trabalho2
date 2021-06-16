from database.person import create_person, list_persons

def create(materia, nota1, nota2):
    if((nota1+nota2)/2>=6.0):
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"
    person = (materia, nota1, nota2, situacao)
    create_person(person)

def get():
    persons = list_persons()
    return persons
