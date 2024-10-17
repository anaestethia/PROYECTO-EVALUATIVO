from codigo.inventario import Inventario
from termcolor import colored

class Personaje:
    def __init__(self, nombre, clase, nivel=1, experiencia=0):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.experiencia = experiencia
        self.inventario = Inventario()

    def __str__(self):
        return f"{self.nombre} - Clase: {self.clase}, Nivel: {self.nivel}, Experiencia: {self.experiencia}"

    def subir_nivel(self):
        self.nivel += 1
        print(colored(f"{self.nombre} ha subido al nivel {self.nivel}!", 'green'))

    def ganar_experiencia(self, cantidad):
        self.experiencia += cantidad
        if self.experiencia >= 100:
            self.subir_nivel()
            self.experiencia -= 100
