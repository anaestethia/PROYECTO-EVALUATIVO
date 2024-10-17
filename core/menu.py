from core.inventario import Item, Inventario
from termcolor import colored

class Menu:
    def __init__(self, juego):
        self.juego = juego
        self.clases_disponibles = ["Guerrero", "Mago", "Arquero", "Ladrón", "Clérigo"]

    def mostrar_menu_principal(self):
        opciones = {
            "1": self.crear_personaje,
            "2": self.juego.listar_personajes,
            "3": self.buscar_personaje,
            "4": self.eliminar_personaje,
            "5": self.modificar_personaje,
            "6": self.salir
        }
        while True:
            self.mostrar_opciones()
            opcion = input(colored("Seleccione una opción: ", 'yellow'))
            accion = opciones.get(opcion, self.opcion_invalida)
            accion()

    def mostrar_opciones(self):
        print(colored("\n--- Menú Principal ---", 'cyan'))
        for i, texto in enumerate(["Crear personaje", "Listar personajes", "Buscar personaje", 
                                   "Eliminar personaje", "Modificar personaje", "Salir"], 1):
            color = 'red' if i == 6 else 'green'
            print(colored(f"{i}. {texto}", color))

    def crear_personaje(self):
        nombre = input(colored("Ingrese el nombre del personaje: ", 'yellow'))
        clase = self.seleccionar_clase()
        personaje = self.juego.crear_personaje(nombre, clase)
        print(f"Personaje creado: {personaje}")

    def seleccionar_clase(self):
        print(colored("Clases disponibles:", 'cyan'))
        for i, clase in enumerate(self.clases_disponibles, 1):
            print(colored(f"{i}. {clase}", 'green'))
        while True:
            clase_elegida = input("Elija el número de la clase: ")
            if clase_elegida.isdigit() and 1 <= int(clase_elegida) <= len(self.clases_disponibles):
                return self.clases_disponibles[int(clase_elegida) - 1]
            print("Opción no válida. Intente de nuevo.")

    def buscar_personaje(self):
        nombre = input(colored("Ingrese el nombre del personaje a buscar: ", 'yellow'))
        personaje = self.juego.buscar_personaje(nombre)
        mensaje = f"Personaje encontrado: {personaje}" if personaje else f"No se encontró el personaje {nombre}."
        print(mensaje)

    def eliminar_personaje(self):
        nombre = input(colored("Ingrese el nombre del personaje a eliminar: ", 'yellow'))
        self.juego.eliminar_personaje(nombre)

    def modificar_personaje(self):
        nombre = input(colored("Ingrese el nombre del personaje a modificar: ", 'yellow'))
        personaje = self.juego.buscar_personaje(nombre)
        if personaje:
            self.modificar_opciones(personaje)
        else:
            print(f"No se encontró el personaje {nombre}.")
        self.juego.guardar_personajes()

    def modificar_opciones(self, personaje):
        print(f"Modificando personaje: {personaje}")
        print(colored("1. Cambiar clase", 'green'))
        print(colored("2. Subir nivel", 'green'))
        print(colored("3. Agregar item", 'green'))
        
        opciones = {
            "1": lambda: self.cambiar_clase(personaje),
            "2": lambda: personaje.subir_nivel(),
            "3": lambda: self.agregar_item(personaje)
        }
        opcion = input(colored("Seleccione una opción: ", 'yellow'))
        accion = opciones.get(opcion, self.opcion_invalida)
        accion()

    def cambiar_clase(self, personaje):
        nueva_clase = self.seleccionar_clase()
        personaje.clase = nueva_clase
        print(f"Clase cambiada a {nueva_clase}")

    def agregar_item(self, personaje):
        nombre_item = input("Ingrese el nombre del item: ")
        tipo_item = input("Ingrese el tipo del item: ")
        valor_item = int(input("Ingrese el valor del item: "))
        nuevo_item = Item(nombre_item, tipo_item, valor_item)
        personaje.inventario.agregar_item(nuevo_item)
        print(f"Item {nombre_item} agregado al inventario")

    def salir(self):
        print("Gracias por jugar. ¡Hasta luego!")
        exit()

    def opcion_invalida(self):
        print("Opción no válida. Intente de nuevo.")
