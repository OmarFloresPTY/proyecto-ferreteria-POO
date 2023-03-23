class Suministar:
    def __init__(self, id, producto,proveedor) -> None:
        self.id = id
        self.producto = producto
        self.proveedor = proveedor
    
    def PrintData(self):
        print("""
        -------------------------------------------------------
        [ Datos de Productos Suministrados por el Proveedor ]
        -------------------------------------------------------
        """)
        
        print(f'id suministro: {self.id}, nombre proveedor = {self.proveedor.nombre + " " + self.proveedor.apellido}, id Provedor = {self.proveedor.id}')
        print(f'Producto suministrado = {self.producto.nombre_producto}, Categoria del Producto = {self.producto.departamento.nombre_departamento}')