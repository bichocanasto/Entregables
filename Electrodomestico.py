#Haz una supeclase llamada Electrodomestico que siga las siguientes condiciones:
#3.1: Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso.
#• Indica que se podrán heredar.
#• Por defecto, el color será blanco, el consumo energético sera F, el precioBase es de $ 100 y el
#peso de 5 kg.
#• Usa constantes para ello.
#• Los colores disponibles son blanco, negro, rojo, azul y gris. No importa si el nombre está en mayúsculas o en minúsculas.->> No pude usar el ENUM siempre me dio error y todos los ejemplos que encontre decian que hay que crear otra clase especifica para el ENUM

from enum import Enum

class Electrodomestico:

    def __init__(self, precioBase = 100, color = "BLANCO", consumoEnergetico = "F", peso = 5):
        self.precioBase = precioBase
        self.color = color
        self.consumoEnergetico = consumoEnergetico
        self.peso = peso

    def __str__(self):
        return f" Precio base: {self.precioBase}, Color: {self.color}, Consumo energetico: {self.consumoEnergetico}, Peso: {self.peso} kg."
    

#GET ALL ATRIBUTOS

    def get_precioBase(self):
        return self.precioBase
    
    def get_color(self):
        return self.color
    
    def get_consumoEnergetico(self):
        return self.consumoEnergetico
    
    def get_peso(self):
        return self.peso


#comprobarConsumoEnergetico(char letra):

    def comprobarConsumoEnergetico(self):
        if self.consumoEnergetico != "A" or "B" or "C" or "D" or "E" or "F":
             self.consumoEnergetico = "F"
        else:
            pass
    

#comprobarColor():

    def comprobarColor(self):
     if self.color != "BLANCO" or "NEGRO" or "ROJO" or "AZUL" or "GRIS":
         self.color = "BLANCO"


#precioFinal():

    def precioFinal(self):
            if self.consumoEnergetico == "A":
                self.precioBase += 100
            elif self.consumoEnergetico == "B":
                self.precioBase += 80
            elif self.consumoEnergetico == "C":
                self.precioBase += 60
            elif self.consumoEnergetico == "D":
                self.precioBase += 50
            elif self.consumoEnergetico == "E":
                self.precioBase += 30
            elif self.consumoEnergetico == "F":
                self.precioBase += 10
            else:
                print("error")    

            if self.peso < 20:
                self.precioBase += 10
            elif self.peso > 20 and self.peso < 49:
                self.precioBase += 50
            elif self.peso > 50 and self.peso < 79:
                self.precioBase += 80
            elif self.peso > 80:
                self.precioBase += 100
            return f"Precio final: {self.precioBase}"

#3.2: Se implantaran varios constructores:
#• Un constructor por defecto.
#• Un constructor con el precio y peso. El resto por defecto.
#• Un constructor con todos los atributos.

#electro00 = Electrodomestico()
#electro01 = Electrodomestico(precioBase= input("Precio base: "), peso= input("Peso: "))
#electro02 = Electrodomestico(150,"AMARILLO","Z",20)


#print(electro00)
#print(electro01)
#print(electro02)

#3.3: Los métodos que implementara serán:
#• Métodos get de todos los atributos.
#• comprobarConsumoEnergetico(char letra): comprueba que la letra es correcta, sino es
#correcta usara la letra por defecto. Se invocará al crear el objeto y no será visible.
#• comprobarColor(String color): comprueba que el color es correcto, sino lo es usa el color por
#defecto.
#• Se invocará al crear el objeto y no será visible.

#print(electro02.get_precioBase())
#print(electro02.get_color())
#print(electro02.get_consumoEnergetico())
#print(electro02.get_peso())

#print(electro02.comprobarConsumoEnergetico())
#print(electro02)

#print(electro02.comprobarColor())
#print(electro02)


#3.3: Los métodos que implementara serán:
#precioFinal(): según el consumo energético, aumentara su precio, y según su tamaño, también.


#print(electro00.precioFinal())

