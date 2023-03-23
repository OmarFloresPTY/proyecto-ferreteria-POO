from producto import Producto
from departamento import Departamento
from proveedor import Proveedor
from cliente import Cliente
from trabajador import Trabajador
from tarjeta import Tarjeta
from suministar import Suministar
from compras import Compras
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
    #producto.PrintData()
    proveedor_cemento = Proveedor("PRO01","Juan","Herrera","9-999-99","999-999","juantio@gmail.com")
    #proveedor_cemento.printData()
    cliente = Cliente("CL01","Omar","Flores","6-666-66","922-222","omar.flores@hotmail.com")
    #cliente.printData()
    pago = Tarjeta("MPT01","12-12-3344-320","234","23/02")
    #print(pago.Numero_Frontal)
    #pago.Numero_Frontal = "13-13-1313-133"
    #print(pago.Numero_Frontal)
    #del pago.Numero_Frontal
    #print(pago.Numero_Frontal) #Aqui se puede hacer un manejo de error. <AttributeError> ya que el atributo y su campo fue eliminado
    suministra = Suministar("SPP01",producto,proveedor_cemento)
    #suministra.PrintData()
    trabajador = Trabajador("TR01","Luis","Ocaña","6-777-7777","888-888","luis.ocana@grupomiguel.com")
    compra = Compras("COM01",2,"22/03/2023",producto,cliente,pago,trabajador)
    compra.PrinData()
    
if __name__ == "__main__":
    main()