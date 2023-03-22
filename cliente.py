from persona import Persona

class Cliente(Persona):
    def __init__(self, id, nombre, apellido, cedula, telefono, correo) -> None:
        super().__init__(id, nombre, apellido, cedula, telefono, correo)
    
    def printDataPersona(self):
        print("Tabla de datos <CLIENTE>")
        print(f'Información Personal: ')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Cedula: {self.cedula}')
        print(f'Telefono: {self.telefono}')
        print(f'Correo: {self.correo}')