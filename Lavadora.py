#3) Crearemos una subclase llamada Lavadora con las siguientes características:
#3.4.1: Su atributo es carga, además de los atributos heredados.
#3.4.2: Por defecto, la carga es de 5 kg. Usa una constante para ello.
#3.4.3: Los constructores que se implementarán serán:
#3.4.4: Un constructor por defecto.
#3.4.5: Un constructor con el precio y peso. El resto por defecto.
#3.4.6: Un constructor con la carga y el resto de los atributos heredados. Recuerda que
#debes llamar al constructor de la clase padre.

from Electrodomestico import Electrodomestico

class Lavadora(Electrodomestico):
    def __init__(self, carga = 5, precioBase = 100, color = "BLANCO", consumoEnergetico = "F", peso = 5):
        Electrodomestico.__init__(self, precioBase, color, consumoEnergetico, peso)
        self.carga = carga

    
    def __str__(self):
        return f"Caracteristicas de la lavadora-> Carga: {self.carga}kg," + super ().__str__()

#GET de carga

    def get_carga(self):
        return self.carga    

#precioFinal(): Si tiene una carga mayor de 30 kg, aumentara el precio $ 50, sino es así no se
#incrementará el precio. Llama al método padre y añade el código necesario. Recuerda que las
#condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio

    def precioFinal(self):
        if int(self.carga) > 30:
            self.precioBase += 50
        return super().precioFinal()


#CONSTRUCTORES

#constructor por defecto. 
#constructor con el precio y peso, el resto por defecto.
#constructor con la carga y el resto de los atributos heredados.

#lavadora00= Lavadora()
#lavadora01= Lavadora(precioBase= input("Precio base: "), peso= input("Peso: "))
#lavadora02= Lavadora(carga= input("Carga: "))

#print(lavadora00)
#print(lavadora01)
#print(lavadora02)

#3.5: Los métodos que se implementara serán:
#Método get de carga.
#precioFinal(): Si tiene una carga mayor de 30 kg, aumentara el precio $ 50, sino es así no se
#incrementará el precio. Llama al método padre y añade el código necesario. Recuerda que las
#condiciones que hemos visto en la clase Electrodomestico también deben afectar al precio

#print(lavadora00.get_carga())
#print(lavadora02.precioFinal())

#Crearemos una subclase llamada Television con las siguientes características:
#3.6.1: Sus atributos son resolución (en pulgadas) y sintonizador TDT (booleano),
#además de los atributos heredados.
#3.6.2: Por defecto, la resolución sera de 20 pulgadas y el sintonizador sera false.
#3.6.3: Los constructores que se implementaran serán:
#3.6.4: Un constructor por defecto.
#3.6.5: Un constructor con el precio y peso. El resto por defecto.
#3.6.6: Un constructor con la resolución, sintonizador TDT y el resto de atributos
#heredados. Recuerda que debes llamar al constructor de la clase padre.