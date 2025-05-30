

class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    def Informacion(self):
        print(f"El {self.marca} {self.modelo} del año {self.año} es un sedán de lujo")

    def Años_desde_que_salio(self):
        self.año += 1
        print(f"El {self.marca} salio en el año {self.año} y ahora tiene un año desde que salio")
