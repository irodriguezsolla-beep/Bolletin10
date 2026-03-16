import pickle
FICHEIRO = "cliente.dat"
class Cliente:
    listaclientes = []
    def __init__(self,ID,nome,telefone):
        self.ID = ID
        self.nombre = nome
        self.telefone = telefone

    @staticmethod
    def cargar_clientes():
        """Carga las tareas desde el archivo"""
        try:
            with open(FICHEIRO, "rb") as f:
                Cliente.listaclientes = pickle.load(f) # asignamos a la lista de clase
        except FileNotFoundError:
            return []

    @staticmethod
    def guardar_clientes():
        """Guarda la lista de clientes en el archivo cliente.dat"""
        with open(FICHEIRO, "wb") as f:
            pickle.dump(Cliente.listaclientes, f)
        print("Clientes guardados correctamente")

    @staticmethod
    def NovoCliente():
        ID = input("Ingrese el ID: ")
        nome = input("Ingres o nome del cliente: ")
        telefone = input("Ingrese el telefone del cliente: ")
        cliente = Cliente(ID,nome,telefone)
        Cliente.listaclientes.append(cliente)
        Cliente.guardar_clientes()
        print("Cliente añadido")

    @staticmethod
    def ModificarDados():
        buscar_id = input("Ingrese el ID del cliente que desea modificar: ")
        for i, cliente in enumerate(Cliente.listaclientes):##Recore la lista
            if cliente.ID == buscar_id:
                cliente.nombre = input("Nuevo nombre: ")
                cliente.telefone = input("Nuevo telefono: ")
                print("Datos modificados correctamente")
                return
            else:
                print("Cliente no encontrado")

    @staticmethod
    def BorrarCliente():
        buscar_id = input("Ingrese el ID del cliente que desea modificar: ")
        # Buscamos el cliente por ID
        for i, cliente in enumerate(Cliente.listaclientes):
            if cliente.ID == buscar_id:
                Cliente.listaclientes.pop(i)  # lo eliminamos de la lista
                Cliente.guardar_clientes()  # guardamos cambios en el archivo
                print(f"Cliente {buscar_id} eliminado correctamente")
                return
            else:
                print("Cliente no encontrado")

    # 1️ Recorremos la lista de clientes usando enumerate:
    #    - 'i' es el índice del cliente en la lista (0, 1, 2…)
    #    - 'cliente' es el objeto Cliente en esa posición
    #    Esto es útil porque necesitamos el índice 'i' para eliminar
    #    el cliente de la lista con .pop(i)
    @staticmethod
    def ListaClientes():
        if not Cliente.listaclientes:
            print("No hay clientes registrados.")
            return
        else:
            print("Clientes registrados correctamente")
            for cliente in Cliente.listaclientes:
                print(f" ID: {cliente.ID}, Nombre: {cliente.nombre}, Teléfono: {cliente.telefone}")
