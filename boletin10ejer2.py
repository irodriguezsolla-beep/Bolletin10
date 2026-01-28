from DataError import DataError
class Data:
    def __init__(self,ano,mes,dia):
        self.setAno(ano)
        self.setMes(mes)
        self.setDia(dia)

    def setAno(self,ano):
        if type(ano) == int:
                 if int(ano)>= 1970 or int(ano)<= 2999:
                     int(ano)
                     self.__ano = ano
                 else:
                    raise DataError(f"El ano {ano} no es valido, tiene que ser mayor o igual a 1970, o menor o igual a 2999")
        else:
            raise TypeError(f"El formato de ano es {type(ano)} y no es entero")
    def getAno(self):
        return self.ano

    def setMes(self,mes):
        if type(mes) == int:
                if int(mes) >= 1 or int(mes) <= 12:
                    self.__mes = mes
                else:
                    raise DataError(f"El mes no puedete tener no puede ser menor de 1 o menor 12")
        else:
            raise TypeError(f"El formato de mes {type(mes)} y no es entero")

    def getMes(self):
        return self.__mes

    def setDia(self, dia):
        if type(dia)== int:
            meses_31_dias = {1, 3, 5, 7, 8, 10, 12}
            meses_30_dias = {4, 6, 9, 11}

            if self.__mes in meses_31_dias:
                max_dia = 31
            elif self.__mes in meses_30_dias:
                max_dia = 30
            elif self.__mes == 2:
            # febrero, revisamos bisiesto
                if (self.__ano % 4 == 0) and ((self.__ano % 100 != 0) or (self.__ano % 400 == 0)):
                    max_dia = 29
                else:
                    max_dia = 28
            else:
                raise DataError(f"El mes {self.__mes} no es válido")

            if 1 <= dia <= max_dia:
                self.__dia = dia
            else:
                raise DataError(f"El día {dia} no concuerda con los días del mes {self.__mes}")
        else:
            raise TypeError("El formato de día no es adecuado, debe ser un entero")
    def getDia(self):
        return self.__dia

    ano = property(getAno,setAno)
    mes = property(getMes,setMes)
    dia = property(getDia,setDia)

    def __str__(self):
        return f"{self.__dia}/{self.__mes}/{self.__ano}"

if __name__ == "__main__":
    try:
        data = Data(2024,6,30)
        print("Data creada correctamente:", data)
    except DataError as e:
        print("Erro de formato na data:", e)
    except TypeError as i:
        print("Erro:",i)