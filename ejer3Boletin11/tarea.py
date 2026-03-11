import pickle
from datetime import date

FICHEIRO = "tarefas.dat"

class Tarefa:
    def __init__(self, nome, descricion, data=None, hora="", duracion="", estado="non feita"):
        self.nome = nome
        self.descricion = descricion
        self.data = data if data else date.today()
        self.hora = hora
        self.duracion = duracion
        self.estado = estado

    def __str__(self):
        return f"{self.nome} | {self.descricion} | {self.data} | {self.hora} | {self.duracion} | {self.estado}"


def cargar_tarefas():
    try:
        with open(FICHEIRO, "rb") as f:
            return pickle.load(f)
    except:
        return []


def gardar_tarefas(tarefas):
    with open(FICHEIRO, "wb") as f:
        pickle.dump(tarefas, f)


def agregar_tarefa():
    nome = input("Nome da tarefa: ")
    descricion = input("Descrición: ")
    hora = input("Hora: ")
    duracion = input("Duración: ")

    tarefa = Tarefa(nome, descricion, hora=hora, duracion=duracion)

    tarefas = cargar_tarefas()
    tarefas.append(tarefa)
    gardar_tarefas(tarefas)

    print("Tarefa agregada.")


def listar_tarefas():
    tarefas = cargar_tarefas()
    for i, t in enumerate(tarefas):
        print(i, "-", t)


def borrar_tarefa():
    tarefas = cargar_tarefas()
    listar_tarefas()
    i = int(input("Número da tarefa a borrar: "))
    tarefas.pop(i)
    gardar_tarefas(tarefas)
    print("Tarefa borrada.")


def modificar_tarefa():
    tarefas = cargar_tarefas()
    listar_tarefas()

    i = int(input("Número da tarefa a modificar: "))
    t = tarefas[i]

    t.nome = input(f"Novo nome ({t.nome}): ") or t.nome
    t.descricion = input(f"Nova descrición ({t.descricion}): ") or t.descricion
    t.estado = input(f"Estado ({t.estado}): ") or t.estado

    gardar_tarefas(tarefas)
    print("Tarefa modificada.")


def menu():
    while True:
        print("\n1. Agregar tarefa")
        print("2. Borrar tarefa")
        print("3. Modificar tarefa")
        print("4. Listar tarefas")
        print("5. Saír")

        op = input("Opción: ")

        if op == "1":
            agregar_tarefa()
        elif op == "2":
            borrar_tarefa()
        elif op == "3":
            modificar_tarefa()
        elif op == "4":
            listar_tarefas()
        elif op == "5":
            break


menu()
