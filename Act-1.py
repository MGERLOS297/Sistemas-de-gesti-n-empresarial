from ast import Del, For


cod_articulo = {}
nombre = {}
descripcion = {}
precio = {}
Articulo = [cod_articulo, nombre, descripcion, precio]

def Alta():  
    print("")

print("------------------------------Alta----------------------------------------")

print("Introduce los datos del articulo.")
cod_articulo = input("Codigo de articulo: ")
nombre = input("Nombre: ")
descripcion = input("Descripcion: ")
precio = input("Precio: ")

Articulo = [cod_articulo, nombre, descripcion, precio]

print("Se a agregado el producto: ")
print(Articulo)
    
    


def Baja():
    print("")

print("--------------------------------Baja------------------------------------------")

for n in Articulo:
    print(n)

eliminar = input("Introduce la posicion que deseas eliminar: ")



Articulo.pop(int(eliminar))
Articulo.insert(int(eliminar),"   ")

print("Se a eliminado correctamente: ")
print(Articulo)




def Modificar():
    print("")

print("-----------------------------Modificar-----------------------------------------")

for n in Articulo:
    print(n)

eliminar = input("Introduce la posicion que deseas modificar: ")
modif = input("introduce el contenido de la celda que deseas modificar: ")


Articulo.pop(int(eliminar))
Articulo.insert(int(eliminar),modif)

print("Se a modificado correctamente: ")
print(Articulo)




def Buscar():
    print("")


print("-------------------------------Buscar-----------------------------------------")

busca = input("Introduce la posicion del contenido que deseas buscar 0 - 3: ")

print(Articulo[int(busca)])



def Mostrar():
    print("")

print("----------------------------Mostrar lista-------------------------------------")

print("esta es la lista actual: ")
print(Articulo)


print("------------------------------------------------------------------------------")
print("                          Fin del programa")
print("------------------------------------------------------------------------------")
