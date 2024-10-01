#2) Haz una clase llamada Password que siga las siguientes condiciones:
#2.3: Ahora, crea una clase ejecutable:
#• Crea un array de Passwords con el tamaño que tu le indiques por teclado.
#• Crea un bucle que cree un objeto para cada posición del array.
#• Indica también por teclado la longitud de los Passwords (antes de bucle).
#• Crea otro array de booleanos donde se almacene si el password del array de Password es o no fuerte (usa el bucle anterior).
#• Al final, muestra la contraseña y si es o no fuerte (usa el bucle anterior). Usa este simple formato:
#• contraseña1 valor_booleano1
#• contraseña2 valor_bololeano2

from Password import Password

class EjecutaPass:
    def __init__(self):
        pass
    

arraypass = []
arraybooleano = []

cant = int(input("Cantidad de contraselas: "))
longitud = int(input("Cantidad de caracteres: "))
for i in range(cant):
    passw00 = Password (longitud)
    passw00.generarPassword()
    arraypass.append(passw00)
    arraybooleano.append(passw00.esFuerte())
    
#print(arraypass)
#print(arraybooleano)  

#me imprime el arraypass: [<Password.Password object at 0x00000224F0EE60C0>, <Password.Password object at 0x00000224F0EE6150>, <Password.Password object at 0x00000224F0C5B2F0>] (el otro array devuelve bien TRUE - FALSE)

#print(passw00)







