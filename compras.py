class Compras():
    def __init__(self,id, cantidad_comprado, fecha_compra,producto,cliente,metodo_pago,trabajador) -> None:
        self.id = id
        self.cantidad_comprado = cantidad_comprado
        self.fecha_compra = fecha_compra
        self.producto = producto
        self.cliente = cliente
        self.metodo_pago = metodo_pago
        self.trabajador = trabajador
