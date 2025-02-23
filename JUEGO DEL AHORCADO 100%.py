# Apertura del juego

print("Bienvenidos al Juego del Ahorcado")

#Ingreso manual del registro del usuario por su nombre
nombre = input("Jugador uno, introduce tu nombre: ") 
print("Hola, " + nombre + "")

#lista de palabras

import random

def obtener_palabra_aleatoria():
    palabras = ["Liga", "Nacional", "Emelec", "Barcelona", "Delfin"]
    palabra_aleatoria = random.choice(palabras)
    return palabra_aleatoria

# Muestrteo en el tablero de palabras secretas y adivinadas 

def mostrar_tablero(palabra_secreta, letras_adivinadas):
    tablero =""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra
        else:
            tablero +="-"    
    print(tablero)

# Lista de palabras aleatorias y numero de intentos de letras

def jugador_ahorcado():
    palabra_secreta =obtener_palabra_aleatoria()    
    letras_adivinadas = []
    intentos_restantes = 6
    
    while intentos_restantes>0:
        mostrar_tablero(palabra_secreta, letras_adivinadas)
        
#  Ingreso al usuario ingresar letra       
        letra =input("Introduce una letra: ")
        
        if letra in letras_adivinadas:
            print('Ya has introducido esa letra. Prueba otra.')
            continue
        
        if letra in palabra_secreta: 
            letras_adivinadas.append(letra)
            if set(letras_adivinadas)==set(palabra_secreta):
                print("Felicidades, has adivinado la palabra")
                break
        else:
            intentos_restantes -=1
            print(f"Letra incorrecta. Te quedan {intentos_restantes}")
    if  intentos_restantes==0:
            print(f"Se te acabaron los intentos. La palabra secreta era: {palabra_secreta}")

# Finalizar juego del ahorcado
jugador_ahorcado()
