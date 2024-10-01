import random

#Haz una clase llamada Password que siga las siguientes condiciones:
#2.1: Que tenga los atributos longitud y contraseña . Por defecto, la longitud será de 8.
#• Los constructores serán los siguiente:
#• Un constructor por defecto.
#• Un constructor con la longitud que nosotros le pasemos.
#• Generará una contraseña aleatoria con esa longitud.


class Password:

    def __init__(self, longitud = 8 , password = ""):
        self.longitud = longitud or input("Longitud: ")
        self.password = password or self.generarPassword()
        

    def __str__(self):
        return f"Longitud: {self.longitud} y contrasela: {self.password}"

#generarPassword(): 


    def generarPassword(self):

        chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ35#36$37%38&39'40(41)42*43+44,45-46.47/48049150251352453554655756857958:59;60<61=62>63?64@65A66B67C68D69E70F71G72H73I74J75K76L77M78N79O80P81Q82R83S84T85U86V87W88X89Y90Z91[9293]94^95_96`97a98b99c100d101e102f103g104h105i106j107k108l109m110n111o112p113q114r115s116t117u118v119w120x121y122z123{124|125}126~"
        chars2 = str(chars)
        password = ""
        self.longitud = int(self.longitud)
        for i in range(self.longitud):
            password += password.join(random.choice(chars2))
        return password


#esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener mas de 2
#mayúsculas, mas de 1 minúscula y mas de 5 números.

    def esFuerte(self):
        mayus = 0
        minus = 0
        nums = 0
        for caracter in str(self.password):
            if caracter.isupper():
                mayus = mayus + 1   
            elif caracter.islower():
                minus = minus + 1
            elif caracter.isdigit():
                nums = nums + 1       
        if mayus > 2 and minus > 1 and nums > 5:
            return True
        else:
            return False 


#Método get para contraseña y otro longitud.
#Método set para longitud.

    def set_longitud(self, longitud):
        self.longitud = longitud

    def get_password(self):
        return self.password
    
    def get_longitud(self):
        return f"Password-> longitud: {self.longitud} y contrasela: {self.password}"



#---------------------------------------------------------    





contra00 = Password()
print(contra00.generarPassword())

#2.2: Los métodos que implementa serán:
#esFuerte(): devuelve un booleano si es fuerte o no, para que sea fuerte debe tener mas de 2
#mayúsculas, mas de 1 minúscula y mas de 5 números.
#generarPassword(): genera la contraseña del objeto con la longitud que tenga.
#Método get para contraseña y longitud.
#Método set para longitud.

contra01 = Password(20)
print(contra01.generarPassword())
print(contra01.esFuerte())



contra01.set_longitud(3) #CHEKEAR CON EL PROFE PORQUE NO ME DEVUELVE PASSWORD DE 3 CARACTERES
print(contra01.get_password())
print(contra01.get_longitud())

#2) Haz una clase llamada Password que siga las siguientes condiciones:
#2.3: Ahora, crea una clase ejecutable:
#• Crea un array de Passwords con el tamaño que tu le indiques por teclado.
#• Crea un bucle que cree un objeto para cada posición del array.
#• Indica también por teclado la longitud de los Passwords (antes de bucle).
#• Crea otro array de booleanos donde se almacene si el password del array de Password es o no
#fuerte (usa el bucle anterior).




