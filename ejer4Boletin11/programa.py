from cliente import Cliente
class Menu:
    def iniciar(self):
        Cliente.cargar_clientes()
        while True:
            print("\nPrograma de xestión de tarefas")
            print("______________________________")
            print("1. Engadir novo cliente")
            print("2. Modificar datos")
            print("3. Dar de baixa clientes")
            print("4. Listar os clientes.")
            print("5. Saír")

            opcion = input("Elixa unha opción: ")
            match opcion:
                case '1':
                    Cliente.NovoCliente()
                case '2':
                    Cliente.ModificarDados()
                case '3':
                    Cliente.BorrarCliente()
                case '4':
                    Cliente.ListaClientes()
                case '5':
                    Cliente.guardar_clientes()
                    print("Saíndo do programa...")
                    break
                case _:
                    print("Opción inválida. Proba outra vez.")

if __name__ == "__main__":
    menu = Menu()
    menu.iniciar()