#from abc import ABC, abstractmethod

class Persona():
    def __init__(self, id, nombre, apellido, cedula, telefono, correo) -> None:
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula
        self.telefono = telefono
        self.correo = correo
    
    #@abstractmethod
    #def printData(self):
        #pass