import json
import os  
from core.personaje import Personaje
from core.inventario import Item, Inventario
from core.menu import Menu
from termcolor import colored

class Juego:
    def __init__(self):
        self.personajes = []
        self.cargar_personajes()
        self.menu = Menu(self)

    def cargar_personajes(self):
        # Crear la carpeta data si no existe
        if not os.path.exists("data"):
            os.makedirs("data")

        try:
            with open("data/personajes.json", "r") as f:
                personajes_data = json.load(f)
                for p in personajes_data:
                    inventario = Inventario()
                    for item_data in p['inventario']:
                        inventario.agregar_item(Item(item_data['nombre'], item_data['tipo'], item_data['valor']))
                    personaje = Personaje(p['nombre'], p['clase'], p['nivel'], p['experiencia'])
                    personaje.inventario = inventario
                    self.personajes.append(personaje)
        except FileNotFoundError:
            print(colored("Archivo de personajes no encontrado. Se creará uno nuevo.", 'red'))

    def guardar_personajes(self):
        with open("data/personajes.json", "w") as f:
            personajes_data = []
            for p in self.personajes:
                personajes_data.append({
                    "nombre": p.nombre,
                    "clase": p.clase,
                    "nivel": p.nivel,
                    "experiencia": p.experiencia,
                    "inventario": [{"nombre": item.nombre, "tipo": item.tipo, "valor": item.valor} for item in p.inventario.items]
                })
            json.dump(personajes_data, f, indent=4)

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
