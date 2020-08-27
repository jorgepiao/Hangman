
from Ahorcado import Ahorcado

ahorcado = Ahorcado()

ahorcado.leerArchivo('ahorcado.txt')
ahorcado.elegirPalabra()

# intentos = int(input('Elige el numero de intentos: '))
intentos = 5
fallos = 0

while fallos < intentos:
    ahorcado.motrarPalabraGuion()

    char = input('\nIngresa una letra: ')

    if ahorcado.adivinarChar(char):
        print('Correcto!!')
        ahorcado.reemplazarGuion(char)
    else:
        print('No!!')
        fallos += 1

    if ahorcado.palabraAdivinada():
        ahorcado.motrarPalabraGuion()
        print('Adivinaste la palabra!!')
        break

    print('Intentos: ' + str(intentos-fallos))

else:
    print('Fallaste!!')



