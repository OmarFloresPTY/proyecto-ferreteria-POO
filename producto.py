class Producto:
    def __init__(self, id, nombre_producto, precio_producto, disponibilidad, marca) -> None:
        self.id = id
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto
        self.disponibilidad = disponibilidad
        self.marca = marca
        self.descripcion = str