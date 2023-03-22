from producto import Producto
from departamento import Departamento

def main():
    construccion = Departamento("D01","Construcción")
    cemento = Producto(
        id = "P01",
        nombre_producto="Cemento Argos",
        precio_producto=7.90,
        disponibilidad=10,
        marca = "Argos",
        departamento = construccion
    )
    cemento.descripcion = "Cemento utilizado para la construcción en general"
    cemento.PrintDataProducto()

    
if __name__ == "__main__":
    main()