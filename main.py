
from Ahorcado import Ahorcado

ahorcado = Ahorcado()

ahorcado.leerArchivo('ahorcado.txt')
ahorcado.elegirPalabra()

# intentos = int(input('Elige el numero de intentos: '))
intentos = 10
fallos = 0

while fallos < intentos:
    ahorcado.motrarPalabraGuion()

    char = input('\nIngresa una letra: ')

    if ahorcado.adivinarChar(char):
        print('\nCorrecto!!')
        ahorcado.reemplazarGuion(char)
    else:
        # print('No!!')
        print()
        fallos += 1

        if fallos == 1:
            print("Quedan 9 intentos")
            print("  --------  ")
        if fallos == 2:
            print("Quedan 8 intentos")
            print("  --------  ")
            print("     O      ")
        if fallos == 3:
            print("Quedan 7 intentos")
            print("  --------  ")
            print("     O      ")
            print("     |      ")
        if fallos == 4:
            print("Quedan 6 intentos")
            print("  --------  ")
            print("     O      ")
            print("     |      ")
            print("    /       ")
        if fallos == 5:
            print("Quedan 5 intentos")
            print("  --------  ")
            print("     O      ")
            print("     |      ")
            print("    / \     ")
        if fallos == 6:
            print("Quedan 4 intentos")
            print("  --------  ")
            print("   \ O      ")
            print("     |      ")
            print("    / \     ")
        if fallos == 7:
            print("Quedan 3 intentos")
            print("  --------  ")
            print("   \ O /    ")
            print("     |      ")
            print("    / \     ")
        if fallos == 8:
            print("Quedan 2 intentos")
            print("  --------  ")
            print("   \ O /|   ")
            print("     |      ")
            print("    / \     ")
        if fallos == 9:
            print("Queda 1 intentos")
            print("  --------  ")
            print("   \ O_|/   ")
            print("     |      ")
            print("    / \     ")
        if fallos == 10:
            print("Perdiste")
            print("  --------  ")
            print("     O_|    ")
            print("    /|\      ")
            print("    / \     ")
            break

    if ahorcado.palabraAdivinada():
        ahorcado.motrarPalabraGuion()
        print('\nADIVINASTE LA PALABRA!!')
        break

    # print('Intentos: ' + str(intentos-fallos))

else:
    print('Fallaste!!')



