from persona import Persona
class Proveedor(Persona):
    def __init__(self, id, nombre, apellido, cedula, telefono, correo) -> None:
        super().__init__(id, nombre, apellido, cedula, telefono, correo)
    
    def printData(self):
        print("Tabla de datos <PROVEEDOR>")
        print(f'Información Personal: ')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'Cedula: {self.cedula}')
        print(f'Telefono: {self.telefono}')
        print(f'Correo: {self.correo}')