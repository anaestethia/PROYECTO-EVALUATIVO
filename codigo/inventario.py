from termcolor import colored

class Item:
    def __init__(self, nombre, tipo, valor, nivel=1):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
        self.nivel = nivel

    def __str__(self):
        return f"{self.nombre} ({self.tipo}) - Valor: {self.valor}, Nivel: {self.nivel}"

class Inventario:
    def __init__(self):
        self.items = []

    def agregar_item(self, item):
        self.items.append(item)

    def remover_item(self, item):
        self.items.remove(item)

    def listar_items(self):
        if not self.items:
            print(colored("El inventario está vacío.", 'red'))
        else:
            for item in self.items:
                print(colored(item, 'cyan'))
