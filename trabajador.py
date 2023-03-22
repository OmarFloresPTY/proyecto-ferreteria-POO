from persona import Persona

class Trabajador(Persona):
    def __init__(self, id_trabajador, nombre, apellido, cedula, telefono, correo) -> None:
        super().__init__(self, id, nombre, apellido, cedula, telefono, correo)
        self.id_trabajador = id_trabajador