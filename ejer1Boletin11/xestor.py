class Xestor:
    def __init__(self,rutafichero):
        self.listaNotas = []
        self.cargarNotas(rutafichero)

    def añadirNota(self):
        Nota = input("Añade una nota:")
        self.listaNotas.append(Nota)
        print("Nota añadida corectamente")

    def mostrarNotas(self):
        for notas in self.listaNotas:
            print(notas)

    def buscarNotas(self, palabra_clave):
        # Creamos unha lista para gardar as notas que coincidan
        notas_encontradas = []
        # Percorremos cada nota na lista
        for nota in self.listaNotas:
            # Se a palabra clave está dentro da nota (sen diferenciar maiúsculas/minúsculas)
            if palabra_clave.lower() in nota.lower():
                # Engadimos a nota á lista de resultados
                notas_encontradas.append(nota)

        # Comprobamos se atopamos algunha nota
        if notas_encontradas:
            print(f"Notas que conteñen '{palabra_clave}':")
            for nota in notas_encontradas:
                print(nota)
        else:
            print(f"Non se atoparon notas que conteñan '{palabra_clave}'.")

    def cargarNotas(self, fichero):
        # Abrimos el archivo en modo lectura ('r')
        # 'with' asegura que se cierre automáticamente al terminar
        with open(fichero, 'r') as fich:
            # Recorremos el archivo línea por línea
            try:
                for linea in fich:
                # 'strip()' elimina saltos de línea y espacios al inicio/final
                # 'append()' añade la línea limpia a la lista de notas
                    self.listaNotas.append(linea.strip())
            except FileNotFoundError:
                print(f"No se encontró el archivo '{fichero}'. Se empezará con una lista vacía.")
    def guardarNotas(self, fichero):
        # Abrimos el archivo en modo escritura ('w')
        # Esto sobrescribe el archivo si ya existía
        with open(fichero, 'w') as fich:
             # Recorremos cada nota en la lista de notas
            for nota in self.listaNotas:
                # Escribimos la nota en el archivo
                # Añadimos '\n' para que cada nota esté en una línea separada
                fich.write(nota + '\n')
            # Mensaje de confirmación
            print("Notas guardadas correctamente")