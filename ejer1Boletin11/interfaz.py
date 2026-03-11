from xestor import Xestor
class Interfaz(Xestor):
    def __init__(self):
        self.xestor = Xestor( 'Notas.txt')
    def menuPrincipal(self):

        while True:
            print("Programa de exstion de almacen")
            print("______________________________")
            print("1.Lista Notas")
            print("2.Engadir Nota")
            print("3.Buscar por palabra clave")
            print("4.Salir")
            option = input("Elixa unha opcion: ")
            match option:
                case '1':
                    self.xestor.mostrarNotas()
                case '2':
                    self.xestor.añadirNota()
                case '3':
                    Palabra = input("Escribe la palabra clave: ")
                    self.xestor.buscarNotas(Palabra)
                case '4':
                    self.xestor.guardarNotas('Notas.txt')
                    break
if __name__=="__main__":

    x = Interfaz()
    x.menuPrincipal()