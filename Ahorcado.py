import random

class Ahorcado:

    def __init__(self):
        self.palabras = []
        self.palabra = ""
        self.palabra_guion = ""

    def leerArchivo(self, nombre_archivo):
        archivo = open(nombre_archivo)

        for linea in archivo:
            linea = linea.strip("\n")
            self.palabras.append(linea)

        archivo.close()

    def elegirPalabra(self):
        min = 0
        max = len(self.palabras) - 1

        self.palabra = self.palabras[random.randint(min,max)]
        self.palabra_guion = "_" * len(self.palabra)

    def adivinarChar(self, char):
        if char in self.palabra and char not in self.palabra_guion:
            return True
        else:
            return False

    def reemplazarGuion(self, char):
        for x in range(len(self.palabra)):
            if self.palabra[x] == char:
                self.palabra_guion = self.palabra_guion[0:x] + char + self.palabra_guion[x+1:]

    def palabraAdivinada(self):
        if "_" not in self.palabra_guion:
            return True
        else:
            return False

    
    def motrarPalabraGuion(self):
        print(self.palabra_guion)


    



