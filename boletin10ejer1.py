from persona import Persona
from ErrorLicencia import LicenciaError
from ErrorDNI import DniError
class Deport(Persona):
    def __init__(self,nome,dni,direcion,deporte,club,licencia):
        super().__init__(nome,dni,direcion)
        self.setDeporte(deporte)
        self.setClub(club)
        self.setLicencia(licencia)

    def setDeporte(self,deporte):
        if type(deporte) == str:
            self.__deporte = deporte
        else:
            raise TypeError(f"El formato no es el corecto")
    def getDeporte(self):
        return self.__deporte

    def setClub(self,club):
        if type(club)== str:
            self.__club = club
        else:
            raise TypeError(f"El formato no es el corecto")
    def getClub(self):
        return self.__club

    def setLicencia(self,licencia):
        if type(licencia) == str:
            if len(licencia) == 13:
                if licencia[:4].isdigit():
                    if licencia[4:7].isalpha() and licencia[4:7].upper() == self.getDeporte()[:3].upper():
                        if licencia[-6:].isdigit():
                            self.__licencia = licencia
                        else:
                            raise LicenciaError (f"Los ultimos 6 digitos tiene que ser números")
                    else:
                        raise LicenciaError (f"Los digitos de de deporte no son correctos ")
                else:
                    raise LicenciaError (f"O los 4 pimeros dijitos o no son 2026 o no son números")
            else:
                raise LicenciaError (f"La cantidad de caractere no es la adecuada tiene que ser 13 caracteres")
        else:
            raise TypeError(f"El formato no es el corecto")
    def getLicencia(self):
        return self.__licencia
    def __str__(self):
        return super().__str__() + ( f"El deporte que hace es: {self.getDeporte()}, pertenecer al club: {self.getClub()}, y su licencia es. {self.getLicencia()}")
if __name__=='__main__':

    try:
        isaac = Deport("Alan","00000000T","Morgadanes","Futball","Real Madrid","2026Fut123456")
        print(isaac)
    except TypeError as t:
        print(t)
    except LicenciaError as l:
        print(l)
    except DniError as e:
        print("Error con p1: ", e)