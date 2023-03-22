from persona import Persona
class Proveedor(Persona):
    def __init__(self, id_proveedor, nombre, apellido, cedula, telefono, correo) -> None:
        super().__init__(id, nombre, apellido, cedula, telefono, correo)
        self.id_proveedor = id_proveedor