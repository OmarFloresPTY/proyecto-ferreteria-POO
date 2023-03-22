from producto import Producto

class Compras(Producto):
    def __init__(self, id_compras, cantidad_comprado, fecha_compra, id_dep, nombre_departamento, id, nombre_producto, precio_producto, disponibilidad, marca) -> None:
        super().__init__(self, id_dep, nombre_departamento, id, nombre_producto, precio_producto, disponibilidad, marca)
        self.id_compras = id_compras
        self.cantidad_comprado = cantidad_comprado
        self.fecha_compra = fecha_compra