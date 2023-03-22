from producto import Producto
from departamento import Departamento
from proveedor import Proveedor
from cliente import Cliente
from trabajador import Trabajador

def main():
    """
        En esta función se crean algunos objetos y se realizan operaciones
        utilizando sus atributos y metodos ya definidos.
    """
    construccion = Departamento("D01","Construcción")
    producto = Producto(
        id = "P01",
        nombre_producto="Cemento",
        precio_producto=7.90,
        disponibilidad=10,
        marca = "Argos",
        departamento = construccion
    )
    producto.descripcion = "Cemento utilizado para la construcción en general"
    producto.PrintDataProducto()
    proveedor_cemento = Proveedor("PRO01","Juan","Herrera","9-999-99","999-999","juantio@gmail.com")
    proveedor_cemento.printDataPersona()
    cliente = Cliente("CL01","Omar","Flores","6-666-66","922-222","omar.flores@hotmail.com")
    cliente.printDataPersona()


    
if __name__ == "__main__":
    main()