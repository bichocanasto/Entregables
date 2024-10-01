#3) Ahora crea una clase Ejecutable que realice lo siguiente:
#3.8.1: Crea un array de Electrodomesticos de 10 posiciones.
#3.8.2: Asigna a cada posición un objeto de las clases anteriores con los valores que
#desees.
#3.8.3: Ahora, recorre este array y ejecuta el método precioFinal().

from Electrodomestico import Electrodomestico
from Lavadora import Lavadora
from Televisor import Televisor

class EjecutableElectro(Electrodomestico):
    def __init__(self, precioBase, color, consumoEnergetico, peso, carga,resolucion, sintonizador):
        Electrodomestico.__init__(self, precioBase, color, consumoEnergetico, peso)
        Lavadora.__init__(self,carga)
        Televisor.__init__(self, resolucion, sintonizador)

    def precioFinal(self):
        for elements in arrayelectro:
            return super().precioFinal()


electro1 = Electrodomestico(200,"NEGRO","D",45)
electro2 = Electrodomestico(500,"ROJO","B",10)
electro3 = Electrodomestico(300,"VERDE","C",20)
lava01 = Lavadora(10,500,"AZUL","B",65)
lava02 = Lavadora(6,250,"BLANCO", "D",90)
lava02 = Lavadora(15,1000,"NEGRA","A",55)
tele01 = Televisor(25,True,250,"AZUL","C",70)
tele02 = Televisor(40,False,400,"VERDE","B",80)
tele03 = Televisor(50,True,800,"BLANCO","A",55)


arrayelectro = []
arrayelectro.append(electro1)
arrayelectro.append(electro2)
arrayelectro.append(electro3)
arrayelectro.append(lava01)
arrayelectro.append(lava02)
arrayelectro.append(tele01)
arrayelectro.append(tele02)
arrayelectro.append(tele03)



print(arrayelectro[0].precioFinal())








#3) Ahora crea una clase Ejecutableque realice lo siguiente:
#3.8.4: Deberás mostrar el precio de cada clase, es decir, el precio de todas las
#televisiones por un lado, el de las lavadoras por otro y la suma de los Electrodomesticos (puedes
#crear objetos Electrodomestico, pero recuerda que Television y Lavadora también son
#electrodomésticos).
#Por ejemplo, si tenemos un Electrodomestico con un precio final de 300, una lavadora de 200 y
#una televisión de 500, el resultado final sera de 1000 (300+200+500) para electrodomésticos, 200
#para lavadora y 500 para televisión.