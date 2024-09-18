print("pprogramacion POO")
# definicion de clases
class perro :
    
    #funciones dentro de class
    def morder (self):
        print ("El perro me mordio")
    def datos_perro(self,nombre,edad):
        print(f"nombre: {nombre} , edad: {edad}")

# zona de cracion de objeto
pitbull=perro()

#zona de uso de objetos
pitbull.datos_perro("bily", 4)
pitbull.morder()
