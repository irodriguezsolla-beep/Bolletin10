from ErrorDNI import DniError
class Persona:
    def __init__(self,nome,dni,direcion):
        self.setNome(nome)
        self.setDni(dni)
        self.setDirecion(direcion)

    def setNome(self, nome):
        if type(nome) == str:
            self.__nome = nome
        else:
            raise TypeError(f"El formato de {nome} no es el corecto")

    def getNome(self):
        return self.__nome

    def setDni(self, dni):
        if type(dni) == str:
            if len(dni) == 9:
                int(dni[:-1])
                if dni[:-1].isdigit():
                    if dni[-1:].isalpha():
                        letraDni = "TRWAGMYFPDXBNJZSQVHLCKE"
                        resto = int(dni[:-1]) % 23
                        letra_correcta = letraDni[resto]
                        if letra_correcta == dni[-1].upper():

                            self.__dni = dni.upper()
                        else:
                            raise DniError(f"La letra no es ta entre las selecionadas para un DNI")
                    else:
                        raise DniError(f"Los 9 primeros digitos no son numeros")
                else:
                    raise DniError(f"El ultimo dígito no es una letra")
            else:
                raise DniError(f"El numero de carateres no es el adecuado")
        else:
            raise TypeError(f"el tipo de {type(dni)} tiene que ser str")

    def getDni(self):
        return self.__dni

    def setDirecion(self,direcion):
        self.direcion = direcion
    def getDirecion(self):
        return self.direcion

    def __str__(self):
        return (f"El nombre es {self.getNome()}, o DNI es: {self.getDni()} y la direción es: {self.getDirecion()}")