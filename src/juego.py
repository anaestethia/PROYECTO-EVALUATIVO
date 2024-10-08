import json
from src.personaje import Personaje
from src.inventario import Item, Inventario
from src.menu import Menu

class Juego:
    def __init__(self):
        self.personajes = []
        self.cargar_personajes()
        self.menu = Menu(self)

    def cargar_personajes(self):
        try:
            with open("data/personajes.txt", "r") as f:
                for linea in f:
                    datos = linea.strip().split(',')
                    nombre, clase, nivel, experiencia = datos[:4]
                    inventario = Inventario()
                    for item_data in datos[4:]:
                        nombre_item, tipo, valor = item_data.split(':')
                        inventario.agregar_item(Item(nombre_item, tipo, int(valor)))
                    personaje = Personaje(nombre, clase, int(nivel), int(experiencia))
                    personaje.inventario = inventario
                    self.personajes.append(personaje)
        except FileNotFoundError:
            print("Archivo de personajes no encontrado. Se creará uno nuevo.")

    def guardar_personajes(self):
        with open("data/personajes.txt", "w") as f:
            for p in self.personajes:
                items = ','.join([f"{item.nombre}:{item.tipo}:{item.valor}" for item in p.inventario.items])
                f.write(f"{p.nombre},{p.clase},{p.nivel},{p.experiencia},{items}\n")

    def crear_personaje(self, nombre, clase):
        personaje = Personaje(nombre, clase)
        self.personajes.append(personaje)
        self.guardar_personajes()
        return personaje

    def listar_personajes(self):
        if not self.personajes:
            print("No hay personajes creados.")
        else:
            for personaje in self.personajes:
                print(personaje)
                print("Inventario:")
                personaje.inventario.listar_items()
                print("--------------------")

    def buscar_personaje(self, nombre):
        for personaje in self.personajes:
            if personaje.nombre.lower() == nombre.lower():
                return personaje
        return None

    def eliminar_personaje(self, nombre):
        personaje = self.buscar_personaje(nombre)
        if personaje:
            self.personajes.remove(personaje)
            self.guardar_personajes()
            print(f"Personaje {nombre} eliminado.")
        else:
            print(f"No se encontró el personaje {nombre}.")

    def iniciar(self):
        self.menu.mostrar_menu_principal()