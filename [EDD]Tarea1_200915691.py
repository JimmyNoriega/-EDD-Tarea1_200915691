import os
import sys

class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creando y trabajando con la lista
class listaSimple: 
    def __init__(self):
        self.head = None
    
    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos a la lista
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
    # Método para eleminar valores
    def delete_node(self, key):
        curr = self.head
        prev = None
        bandera = "false"
        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

        if curr.data == key: #definir si existe o no valor
            print ("Eliminado Correctamente")
        else:
            print ("Valor a eliminar no existe")

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next

    # Método para modificar un valor de la lista
    def modify_node(self, key, nuevo):
        if self.is_empty() == True:
          print("lista vacia")

        if self.is_empty() == False:
            curr = self.head
            prev = None
            banderaAux = "false"
            while curr and curr.data != key:
                prev = curr
                curr = curr.next
                
            if prev is None:
                self.head = curr
                curr.data = nuevo

            elif curr:
                curr.data = nuevo
            


       

s = listaSimple() # Instancia de la clase

def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una opcion")
	print ("\t1 - Agregar valor")
	print ("\t2 - Modificar valor")
	print ("\t3 - Eliminar valor")
	print ("\t4 - Listar valores")
	print ("\t9 - salir")

while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("Seleccione opcion a realizar >> ")
 
	if opcionMenu=="1":
		print ("")
		valor = input("valor agregar es: >>")
		s.add_at_end(valor)
		print("Agregado Correctamente >>")
		input("Presione cualquie tecla para continuar")
	elif opcionMenu=="2":
		print ("")
		valor = input("valor a modificar es: >>")
		nuevo = input("nuevo valor es: >>")
		s.modify_node(valor,nuevo)
		print("operacion realizada")
		input("Presione cualquie tecla para continuar")
	elif opcionMenu=="3":
		print ("")
		valor = input("valor a eliminar es:")
		s.delete_node(valor)
		input("Presione cualquie tecla para continuar")
	elif opcionMenu=="4":
		print ("valores:")
		s.print_list()
		print ("")
		input("Presione cualquie tecla para continuar")
	elif opcionMenu=="9":
		break
                
	else:
		print ("")
		input("No has pulsado ninguna opcion correcta...\npulsa una tecla para continuar")

