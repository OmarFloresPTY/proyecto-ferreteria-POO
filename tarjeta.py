from metodo_de_pago import Metodo_de_Pago

class Tarjeta(Metodo_de_Pago):
    def __init__(self, id, numero_frontal, cvv, fecha_vencimiento) -> None:
        super().__init__(id)
        self.numero_frontal = numero_frontal
        self.cvv = cvv
        self.fecha_vencimiento = fecha_vencimiento