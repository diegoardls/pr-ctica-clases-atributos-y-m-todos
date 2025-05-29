#main.py

from Vehiculos import Vehiculo

vehiculo1 = Vehiculo("Nissan", "maxima", 2024)
vehiculo2 = Vehiculo("nissan", "sentra", 2024)

vehiculo1.Informacion()
vehiculo2.Informacion()

vehiculo1.Años_desde_que_salio()
vehiculo2.Años_desde_que_salio()