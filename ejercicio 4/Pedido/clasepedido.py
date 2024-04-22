class Pedido:
    __patente = str
    __id_pedido = int
    __comida = str
    __tiempo_est = int
    __tiempo_real = int
    __precio = float

    def __init__ (self, pat, id, com, t_est, imp):
        self.__patente = pat
        self.__id_pedido = id
        self.__comida = com
        self.__tiempo_est = t_est
        self.__tiempo_real = 0
        self.__precio = imp
