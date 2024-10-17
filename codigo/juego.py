import json
from codigo.personaje import Personaje
from codigo.inventario import Item, Inventario
from codigo.menu import Menu
from termcolor import colored

class Juego:
    def __init__(self):
        self.personajes = []
        self.cargar_personajes()
        self.menu = Menu(self)

    def cargar_personajes(self):
        try:
            with open("data/personajes.txt", "r") as f:
                for linea in f:
                    self.procesar_linea(linea.strip())
        except FileNotFoundError:
            print(colored("Archivo de personajes no encontrado. Se creará uno nuevo.", 'red'))

    def procesar_linea(self, linea):
        datos = linea.split(',')
        nombre, clase, nivel, experiencia = datos[:4]
        inventario = Inventario()
        for item_data in datos[4:]:
            self.procesar_item(item_data, inventario)
        personaje = Personaje(nombre, clase, int(nivel), int(experiencia))
        personaje.inventario = inventario
        self.personajes.append(personaje)

    def procesar_item(self, item_data, inventario):
        if ':' in item_data:
            partes = item_data.split(':')
            if len(partes) == 3:
                nombre_item, tipo, valor = partes
                inventario.agregar_item(Item(nombre_item, tipo, int(valor)))
            else:
                print(f"Advertencia: formato de item incorrecto: {item_data}")

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
            print(colored("No hay personajes creados.", 'red'))
        else:
            for personaje in self.personajes:
                print(colored(personaje, 'cyan'))
                print(colored("Inventario:", 'cyan'))
                personaje.inventario.listar_items()
                print(colored("--------------------", 'cyan'))

    def buscar_personaje(self, nombre):
        return next((p for p in self.personajes if p.nombre.lower() == nombre.lower()), None)

    def eliminar_personaje(self, nombre):
        personaje = self.buscar_personaje(nombre)
        if personaje:
            self.personajes.remove(personaje)
            self.guardar_personajes()
            print(f"Personaje {nombre} eliminado.")
        else:
            print(colored(f"No se encontró el personaje {nombre}.", 'red'))

    def iniciar(self):
        self.menu.mostrar_menu_principal()
