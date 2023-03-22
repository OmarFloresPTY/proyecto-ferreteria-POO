from metodo_de_pago import Metodo_de_Pago

class Dinero_Cash(Metodo_de_Pago):
    def __init__(self,id,cantidad) -> None:
        super().__init__(id)
        self.cantidad = cantidad