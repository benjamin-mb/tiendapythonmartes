from random import *
nombreVendedor=None 
productos=[]

opcion=100

print("Mercado")
print("********")
print("1. Crear lista mercado")
print("2. Ver Lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("Presiona 5 para salir")
while opcion != 5:
    opcion=int(input("Digita una opcion: "))
    if opcion == 1:
        print("Bienvenido a la creacion de tu lista de mercado")
        
        #creando claves y valores de un diccionario
        producto={
        "id":randint(0,1000), 
        "nombre":input("Digita el nombre del producto: "),
        "precio":int(input("Digita el precio del producto: ")),
        "cantidad":int(input("Cuantos elementos de este producto vas a llevar: ")),
        "presentacion":input("Cual presentacion llevaras? ")
        }
        #mostrando mi diccionario
        #print(producto)
        
        #poblando una lista (agrgando elementos a una lista)
        productos.append(producto)
        print(producto)
        
        
        
    elif opcion==2:
        #utilizando ciclos for para recorrer listas
        for product in productos:
            print (product["nombre"])
    elif opcion==3:
        #1.encontrar elemento
        for product in productos:
            print(product["id"]+["nombre"])
        #2.seleccion elemento
        
        #3.acceder a la propiedad y editarla
        print("estoy en la 3")
    elif opcion==4:
        print("estoy en la 4")
    else:
        print("Opcion no valida")
        