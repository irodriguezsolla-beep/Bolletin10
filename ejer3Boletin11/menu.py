from tarea import Tarefa

class Menu:
    def iniciar(self):
        while True:
            print("\nPrograma de xestión de tarefas")
            print("______________________________")
            print("1. Listar tarefas")
            print("2. Engadir tarefa")
            print("3. Borrar tarefa")
            print("4. Modificar tarefa")
            print("5. Saír")

            opcion = input("Elixa unha opción: ")
            match opcion:
                case '1':
                    Tarefa.listar_tarefas()
                case '2':
                    Tarefa.agregar_tarefa()
                case '3':
                    Tarefa.borrar_tarefa()
                case '4':
                    Tarefa.modificar_tarefa()
                case '5':
                    print("Saíndo do programa...")
                    break
                case _:
                    print("Opción inválida. Proba outra vez.")


if __name__ == "__main__":
    menu = Menu()
    menu.iniciar()