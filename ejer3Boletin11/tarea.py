
import pickle
from datetime import date

FICHEIRO = "tarefas.dat"  # Archivo donde se guardarán las tareas
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

    # ---------------- Métodos estáticos ----------------
    @staticmethod
    def cargar_tarefas():
        """Carga las tareas desde el archivo"""
        try:
            with open(FICHEIRO, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def gardar_tarefas(tarefas):
        """Guarda las tareas en el archivo"""
        with open(FICHEIRO, "wb") as f:
            pickle.dump(tarefas, f)

    @staticmethod
    def agregar_tarefa():
        """Agregar una nueva tarea"""
        nome = input("Nome da tarefa: ")
        descricion = input("Descrición: ")
        hora = input("Hora: ")
        duracion = input("Duración: ")

        tarefa = Tarefa(nome, descricion, hora=hora, duracion=duracion)

        tarefas = Tarefa.cargar_tarefas()
        tarefas.append(tarefa)
        Tarefa.gardar_tarefas(tarefas)

        print("Tarefa agregada.")

    @staticmethod
    def listar_tarefas():
        """Mostrar todas las tareas"""
        tarefas = Tarefa.cargar_tarefas()
        if not tarefas:
            print("Non hai tarefas.")
            return
        for i, t in enumerate(tarefas):
            print(i, "-", t)

    @staticmethod
    def borrar_tarefa():
        """Borrar una tarea por índice"""
        tarefas = Tarefa.cargar_tarefas()
        Tarefa.listar_tarefas()
        try:
            i = int(input("Número da tarefa a borrar: "))
            tarefas.pop(i)
            Tarefa.gardar_tarefas(tarefas)
            print("Tarefa borrada.")
        except (IndexError, ValueError):
            print("Número inválido.")

    @staticmethod
    def modificar_tarefa():
        """Modificar una tarea por índice"""
        tarefas = Tarefa.cargar_tarefas()
        Tarefa.listar_tarefas()
        try:
            i = int(input("Número da tarefa a modificar: "))
            t = tarefas[i]

            t.nome = input(f"Novo nome ({t.nome}): ") or t.nome
            t.descricion = input(f"Nova descrición ({t.descricion}): ") or t.descricion
            t.estado = input(f"Estado ({t.estado}): ") or t.estado

            Tarefa.gardar_tarefas(tarefas)
            print("Tarefa modificada.")
        except (IndexError, ValueError):
            print("Número inválido.")