class Producto():
    codigo = 1020
    nombre = "pantene"
    precio = 20
    unidades = 3
    total = precio * unidades

    def __init__(self,nombre,precio,unidades):
        self.nombre = nombre
        self.precio = precio
        self.unidades = unidades
        self.total = precio * unidades


    def presentacion(self):
        print(self.nombre,"Para un cabello doblemente suave")
    
    def calcularTotal(self):
        print("su total es:",self.total)

     

producto1 = Producto("Pantene",20,3)
producto1.calcularTotal()
producto1.presentacion()