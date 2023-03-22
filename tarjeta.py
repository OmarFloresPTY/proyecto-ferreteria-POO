from metodo_de_pago import Metodo_de_Pago

class Tarjeta(Metodo_de_Pago):
    def __init__(self, id, numero_frontal, cvv, fecha_vencimiento) -> None:
        super().__init__(id)
        self.__numero_frontal = numero_frontal
        self.__cvv = cvv
        self.__fecha_vencimiento = fecha_vencimiento

    @property
    def Numero_Frontal(self):
        #El getter se activa cuando se hace el llamado de la funcion o impresion del numero frontal, funciona igual para los demas getter
        return self.__numero_frontal
        
    @Numero_Frontal.setter
    def Numero_Frontal(self, nuevo):
        print("Modificando el numero frontal de la tarjeta de crédito...")
        print(f'Se ha cambiado el numero frontal {self.__numero_frontal} a {nuevo}')
        self.__numero_frontal = nuevo
        
    @Numero_Frontal.deleter
    def Numero_Frontal(self):
        print("Borrando número frontal de tarjeta de Crédito")
        del self.__numero_frontal

    @property
    def CVV(self):
        return self.__cvv
        
    @CVV.setter
    def CVV(self, nuevo):
        print("Modificando CVV de la tarjeta....")
        print(f'Se ha modificado con exito!')
        self.__cvv = nuevo
        
    @CVV.deleter
    def CVV(self):
        print("Eliminado el CVV de la tarjeta....")
        print("Se ha eliminado con exito....")
        del self.__cvv
        
    @property
    def Fecha_Vencimiento(self):
        return self.__fecha_vencimiento
        
    @Fecha_Vencimiento.setter
    def Fecha_Vencimiento(self, nuevo):
        print("Se ha modificado con exito la fecha de vencimiento de la tarjeta!")
        self.__fecha_vencimiento = nuevo
        
    @Fecha_Vencimiento.deleter
    def Fecha_Vencimiento(self):
        print("Se ha eliminado la fecha de vencimiento de la tarjeta con exito!")
        del self.__fecha_vencimiento