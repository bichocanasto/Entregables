import enum
import random

#SOLO FALTA VER TEMA ENUM, EL RESTO TODO OK
class Persona:
        
    def __init__(self, nombre = None, edad = 0, sexo = "", peso = 0, altura = 0, DNI = None):
        self.__nombre = nombre
        self.__edad = edad
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__DNI = DNI or self.generaDNI()


#calcularIMC():

    def get_imc(self):
        INFRAPESO = -1 #CONSTANTES
        BAJOPESO = 0 #CONSTANTES
        SOPBREPESO = 1 #CONSTANTES
        calcularimc = float(self.__peso)/float(self.__altura**2)
        if float(calcularimc)< 20:
            return("Indice de masa corporal:", INFRAPESO)
        elif float(calcularimc) > 20 and float(calcularimc) < 25:
            return("Indice de masa corporal:", BAJOPESO)
        elif float(calcularimc) > 25:
            return("Indice de masa corporal:", SOPBREPESO)
          

#esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano., 
#comprobarSexo(char sexo): comprueba que el sexo introducido es correcto. Si no es correcto, sera H. No sera visible al exterior.
#toString(): devuelve toda la información del objeto. 
    
    
    def esMayorDeEdad(self):
        if self.__edad > 18:
            return True
        else:
            return False

    def comprobarSexo(self):

        #ver con el profe porque si no es una clase no se
        #self.__sexo = enum{"M", "H", "X"}
        if self.__sexo == "M":
            pass
        elif self.__sexo == "H":
            pass
        elif self.__sexo =="X":
            pass
        else:
            self.__sexo = "H"
        return self.__sexo
   
    def __str__(self):
        return f"Nombre: {self.__nombre}, edad: {self.__edad} años, sexo: {self.__sexo}, peso: {self.__peso}kg, altura: {self.__altura}cm, DNI: {self.__DNI}"
    

#generaDNI()

    def generaDNI(self):
        self.__DNI = random.randrange(10000000,99999999)
        return self.__DNI
    

#INPUTS Y SET + GET

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad
    
    def set_DNI(self, DNI):
        self.__DNI = DNI
    
    def set_sexo(self, sexo):
        self.__sexo = sexo
    
    def set_peso(self, peso):
        self.__peso = peso
    
    def set_altura(self, altura):
        self.__altura = altura
       

    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def get_DNI(self):
        return self.__DNI
    
    def get_sexo(self):
        return self.__sexo
    
    def get_peso(self):
        return self.__peso
    
    def get_altura(self):
        return self.__altura


#--------------

#PJS

persona00= Persona()
persona01= Persona(nombre= "Pirulin", edad=23, sexo= "X")
persona02= Persona(nombre= "Pedrin",edad=3, DNI=4564322,sexo ="M", peso = 10,altura=180) 
persona03= Persona(nombre= "Pascual", edad=43, DNI=3224564, sexo= "P",peso= 250,altura=120)

#CONSTRUCTORES

print(persona00) #constructor por defecto. 
print(persona01) #constructor con el nombre, edad y sexo, el resto por defecto.
print(persona02) #constructor con todos los atributos como parámetro.

#calcularIMC(): calcular si la persona esta en su peso ideal (peso en kg/(altura^2 en m)), si esta fórmula devuelve un valor menor que 20, la función devuelve un -1, si devuelve un número entre 20 y 25 (incluidos), significa que esta por debajo de su peso ideal la función devuelve un 0 y si devuelve un valor mayor que 25 significa que tiene sobrepeso, la función devuelve un 1. Te recomiendo que uses constantes para devolver estos valores.

print(persona02.get_imc()) #no me da bien em m, pero en cm si volver a probar porque quiere en cm el profe
print(persona03.get_imc())

#esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano., 
#comprobarSexo(char sexo): comprueba que el sexo introducido es correcto. Si no es correcto, sera H. No sera visible al exterior.
#toString(): devuelve toda la información del objeto.

print(persona02.esMayorDeEdad()) 
print(persona02.comprobarSexo()) 
print(persona02.__str__())
print(persona03.esMayorDeEdad()) 
print(persona03.comprobarSexo())
print(persona03.__str__())

#1.3:generaDNI(): genera un número aleatorio de 8 cifras, genera a partir de este su número su letra correspondiente.--> KE LETRA TIENE EL DNI KEDICE
#Este método será invocado cuando se construya el objeto. Puedes dividir el método para que te sea más fácil.
#No será visible al exterior.
#Métodos set de cada parámetro, excepto de DNI.

print(persona03.generaDNI()) #con __ adelante no seria visible para el exterior, lo saco para que no de error de visualizacion


#1.4.1: Pide por teclado el nombre, la edad, sexo, peso y altura.
#1.4.2: Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura y el último por defecto, para este último utiliza los métodos set para darle a los atributos un valor.


persona04= Persona(nombre= input("Nombre: "), edad= int(input("Edad: ")), sexo= input("Sexo: "), peso= int(input("Peso: ")), altura = int(input("Altura: ")))
persona05= Persona(nombre= input("Nombre: "), edad= (int(input("Edad: "))), sexo= input("Sexo: "))

print(persona04)
print(persona05)
print(persona00)
persona00.set_nombre("Pipi")
persona00.set_edad(33)
persona00.set_altura(66)
print(persona00.get_nombre())
print(persona00.get_edad())
print(persona00.get_altura())
print(persona00)
