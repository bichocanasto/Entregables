from Electrodomestico import Electrodomestico


class Televisor(Electrodomestico):
    def __init__(self, resolucion = 20, sintonizador = False,precioBase = 100, color = "BLANCO", consumoEnergetico = "F", peso = 5):
        Electrodomestico.__init__(self, precioBase, color, consumoEnergetico, peso)
        self.resolucion = resolucion
        self.sintonizador = sintonizador

    def __str__(self):
        return f"Caracteristicas del televisor-> Resolucion: {self.resolucion} pulgadas, Sintonizador TDT: {self.sintonizador}" + super ().__str__()


#get de resolución y sintonizador TDT

    def get_resolucion(self):
        return self.resolucion
    
    def get_sintonizador(self):
        return self.sintonizador
    
#precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementará el precio un 30% y si
#tiene un sintonizador TDT incorporado, aumentara $ 50. Recuerda las condiciones que hemos visto en la clase
#Electrodomesticotambién deben afectar al precio.

    def precioFinal(self):
        altreinta = (self.precioBase*30)/100
        if int(self.resolucion) > 40:
            self.precioBase += altreinta
        if self.sintonizador == True:
            self.precioBase *= 50
        return super().precioFinal()




#CONSTRUCTORES
#Un constructor por defecto.
#Un constructor con el precio y peso. El resto por defecto.
#Un constructor con la resolución, sintonizador TDT y el resto de atributos

#televisor00= Televisor()
#televisor01= Televisor(precioBase= input("Precio base: "), peso= input("Peso: "))
#televisor02= Televisor(peso= 100,resolucion= 30, sintonizador= True)

#print(televisor00)
#print(televisor01)
#print(televisor02)


#3.7: Los métodos que se implementara serán:
#Método get de resolución y sintonizador TDT.
#precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementará el precio un 30% y si
#tiene un sintonizador TDT incorporado, aumentara $ 50. Recuerda las condiciones 
#que hemos visto en la clase Electrodomestico también deben afectar al precio.

#print(televisor02.get_resolucion())
#print(televisor02.get_sintonizador())
#print(televisor02.precioFinal())
