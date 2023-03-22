from persona import Persona

class Cliente(Persona):
    def __init__(self, id_cliente, nombre, apellido, cedula, telefono, correo) -> None:
        super().__init__(self, id, nombre, apellido, cedula, telefono, correo)
        self.id_cliente = id_cliente