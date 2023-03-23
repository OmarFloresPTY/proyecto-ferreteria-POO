class Compras():
    def __init__(self,id, cantidad_comprado, fecha_compra,producto,cliente,metodo_pago,trabajador) -> None:
        self.id = id
        self.cantidad_comprado = cantidad_comprado
        self.fecha_compra = fecha_compra
        self.producto = producto
        self.cliente = cliente
        self.metodo_pago = metodo_pago
        self.trabajador = trabajador

    def PrinData(Self):
        print("""
        -------------------------------------------------------
        [ INFORME DE LA COMPRA DEL CLIENTE CON LA FERRETERIA]
        -------------------------------------------------------
        """)
        print(f'Producto Comprado = {Self.producto.nombre_producto}')
        print(f'Cantidad Comprado = {Self.cantidad_comprado}')
        print(f'Precio Producto = {Self.producto.precio_producto}')
        print(f'Total = {Self.cantidad_comprado * Self.producto.precio_producto}')
        print(f'Cliente = {Self.cliente.nombre + " " + Self.cliente.apellido}')
        print(f'Trabajor asociado = {Self.trabajador.nombre + " " + Self.trabajador.apellido}')
        print(f'Fecha de la compra = {Self.fecha_compra}')
        print(f'Metodo de Pago = {Self.metodo_pago.descripcion}')

