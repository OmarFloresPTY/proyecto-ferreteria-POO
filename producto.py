from departamento import Departamento

class Producto(Departamento):
    def __init__(self, id_dep, nombre_departamento, id, nombre_producto, precio_producto, disponibilidad, marca) -> None:
        super().__init__(id_dep, nombre_departamento)
        self.id = id
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto
        self.disponibilidad = disponibilidad
        self.marca = marca
        self.descripcion = str