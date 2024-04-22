from clasepedido import Pedido
import csv

class gestor_p:
    __lista_p = []

    def __init__ (self):
        self.__lista_p
    
    def agregar_p (self, unpedido):
        self.__lista_p.append (unpedido)

    def leer_datos (self):
        archivo = open ('pedidos.csv')
        reader = csv.reader (archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera == True:
                bandera = False
            else:
                pat_asign = fila[0]
                id_p = fila [1]
                comida = fila[2]
                t_est = fila[3]
                precio = [4]
                unpedido = Pedido (pat_asign, id_p, comida, t_est, precio)
                self.agregar_p (unpedido)