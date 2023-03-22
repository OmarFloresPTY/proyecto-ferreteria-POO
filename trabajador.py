from persona import Persona

class Trabajador(Persona):
    def __init__(self, id_trabajador, nombre, apellido, cedula, telefono, correo) -> None:
        super().__init__(id, nombre, apellido, cedula, telefono, correo)
        self.id_trabajador = id_trabajador
    
    def printDataPersona(self):
        print("Tabla de datos <TRABAJADOR>")
        print(f'Información Personal: ')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Cedula: {self.cedula}')
        print(f'Telefono: {self.telefono}')
        print(f'Correo: {self.correo}')