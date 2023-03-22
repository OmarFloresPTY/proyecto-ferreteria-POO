from departamento import Departamento

class Producto(Departamento):
    
    def __init__(self,id, nombre_producto, precio_producto, disponibilidad, marca, departamento) -> None:
        self.id = id
        self.nombre_producto = nombre_producto
        self.precio_producto = precio_producto
        self.disponibilidad = disponibilidad
        self.marca = marca
        self.departamento = departamento
        self.descripcion = str
    
    def PrintDataProducto(self):
        print("IMPRESION DE DATOS DEL PRODUCTO")
        print("---------------------------------")
        print(f'id = {self.id} --> nombre producto = {self.nombre_producto} --> precio = {self.precio_producto}')
        print(f'disponibilidad = {self.disponibilidad} --> marca = {self.marca}')
        print(f'Departamento = {self.departamento.nombre_departamento} --> id Departamento = {self.departamento.id_dep}')