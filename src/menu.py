from src.inventario import Item, Inventario

class Menu:
    def __init__(self, juego):
        self.juego = juego
        self.clases_disponibles = ["Guerrero", "Mago", "Arquero", "Ladrón", "Clérigo"]

    def mostrar_menu_principal(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Crear personaje")
            print("2. Listar personajes")
            print("3. Buscar personaje")
            print("4. Eliminar personaje")
            print("5. Modificar personaje")
            print("6. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.crear_personaje()
            elif opcion == "2":
                self.juego.listar_personajes()
            elif opcion == "3":
                self.buscar_personaje()
            elif opcion == "4":
                self.eliminar_personaje()
            elif opcion == "5":
                self.modificar_personaje()
            elif opcion == "6":
                print("Gracias por jugar. ¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

    def crear_personaje(self):
        nombre = input("Ingrese el nombre del personaje: ")
        
        print("Clases disponibles:")
        for i, clase in enumerate(self.clases_disponibles, 1):
            print(f"{i}. {clase}")
        
        while True:
            clase_elegida = input("Elija el número de la clase: ")
            if clase_elegida.isdigit() and 1 <= int(clase_elegida) <= len(self.clases_disponibles):
                clase = self.clases_disponibles[int(clase_elegida) - 1]
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        
        personaje = self.juego.crear_personaje(nombre, clase)
        print(f"Personaje creado: {personaje}")

    def buscar_personaje(self):
        nombre = input("Ingrese el nombre del personaje a buscar: ")
        personaje = self.juego.buscar_personaje(nombre)
        if personaje:
            print(f"Personaje encontrado: {personaje}")
        else:
            print(f"No se encontró el personaje {nombre}.")

    def eliminar_personaje(self):
        nombre = input("Ingrese el nombre del personaje a eliminar: ")
        self.juego.eliminar_personaje(nombre)

    def modificar_personaje(self):
        nombre = input("Ingrese el nombre del personaje a modificar: ")
        personaje = self.juego.buscar_personaje(nombre)
        if personaje:
            print(f"Modificando personaje: {personaje}")
            print("1. Cambiar clase")
            print("2. Subir de nivel")
            print("3. Agregar item al inventario")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                print("Clases disponibles:")
                for i, clase in enumerate(self.clases_disponibles, 1):
                    print(f"{i}. {clase}")
                while True:
                    clase_elegida = input("Elija el número de la nueva clase: ")
                    if clase_elegida.isdigit() and 1 <= int(clase_elegida) <= len(self.clases_disponibles):
                        nueva_clase = self.clases_disponibles[int(clase_elegida) - 1]
                        personaje.clase = nueva_clase
                        print(f"Clase cambiada a {nueva_clase}")
                        break
                    else:
                        print("Opción no válida. Intente de nuevo.")
            
            elif opcion == "2":
                personaje.subir_nivel()
                print(f"Personaje subido al nivel {personaje.nivel}")
            
            elif opcion == "3":
                nombre_item = input("Ingrese el nombre del item: ")
                tipo_item = input("Ingrese el tipo del item: ")
                valor_item = int(input("Ingrese el valor del item: "))
                nuevo_item = Item(nombre_item, tipo_item, valor_item)
                personaje.inventario.agregar_item(nuevo_item)
                print(f"Item {nombre_item} agregado al inventario")
            
            else:
                print("Opción no válida.")
        else:
            print(f"No se encontró el personaje {nombre}.")

        self.juego.guardar_personajes()