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
                     self.ano = ano
                 else:
                    raise DataError(f"El ano {ano} no es valido, tiene que ser mayor o igual a 1970, o menor o igual a 2999")
        else:
            raise TypeError(f"El formato de ano es {type(ano)} y no es entero")
    def getAno(self):
        return self.ano

    def setMes(self,mes):
        if type(mes) == int:
                if int(mes) >= 1 or int(mes) <= 12:
                    self.mes = mes
                else:
                    raise DataError(f"El mes no puedete tener no puede ser menor de 1 o menor 12")
        else:
            raise TypeError(f"El formato de mes {type(mes)} y no es entero")

    def eBisesto(self):
        return (self.ano % 4 == 0 and self.ano % 100 != 0) or (self.ano % 400 == 0)

    def setDia(self, dia):
        if not isinstance(dia, int):
            raise DataError("O día debe ser un enteiro")
        # Días máximos por mes
        dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # Febreiro en ano bisesto
        if self.mes == 2 and self.eBisesto():
            max_dia = 29
        else:
            max_dia = dias_mes[self.mes - 1]
        if dia < 1 or dia > max_dia:
            raise DataError(f"O día {dia} non é válido para o mes {self.mes} no ano {self.ano}")
        self.dia = dia


    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

if __name__ == "__main__":
    try:
        dia = int(input("Introduce o día: "))
        mes = int(input("Introduce o mes: "))
        ano = int(input("Introduce o ano: "))

        data = Data(dia, mes, ano)
        print("Data creada correctamente:", data)

    except DataError as e:
        print("Erro de formato na data:", e)

    except ValueError:
        print("Erro: debes introducir números enteiros")

    except Exception as e:
        print("Erro inesperado:", e)