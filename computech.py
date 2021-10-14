#import datetime
import productos
import vendedores
import ventas
from pathlib import Path

lista_productos = [ ]

lista_vendedores = [
    ["1", "2", "3",'4','5','6','7','8','9','10'],                                   #Vendedor ID
    ['juan perez', 'mariana lopez', 'pedro gonzalez','alejadro martinez', 'daniel alejandro', 'miguel alvarez','jose hernandez', 'juan serrano', 'josue rodriguez','pedro sanchez']  #Nombre
]

lista_ventas = [
    [],                                  #Vendedor ID
    [],                                  #Producto ID
    [], #Fecha
    [],                                  #Cantidad
    []                  #Total
]

# print_matriz
# matriz: la matriz que quieres desplegar en la terminal
# nombre_columnas: una lista con los nombres de cada columna de la matriz
def print_matriz(matriz, nombre_columnas):
    bigger_size = []
    for nombre in nombre_columnas:
        bigger_size.append(len(nombre))
    
    for idx, fila in enumerate(matriz):
        for element in fila:
            if len(str(element)) > bigger_size[idx]:
                bigger_size[idx] = len(str(element))

    for i in range(len(nombre_columnas)):
        print(nombre_columnas[i].center(bigger_size[i] + 2), end = "")
    print()
    
    for i in range(len(matriz[0])):
        for j in range(len(nombre_columnas)):
            print(str(matriz[j][i]).title().center(bigger_size[j] + 2), end = "")
        print()

# buscar_elemento
# matriz: la tabla en la que deseas buscar
# columna: la columna de la tabla en la que deseas buscar
# valor: el valor que deseas buscar
# return: el indice del valor en la tabla o -1 si no esta
#              lista_vendedores, 1, mariana lopez
def buscar_elemento(matriz, columna, valor):
    if valor in matriz[columna]:
        return matriz[columna].index(valor)
    else:
        return -1

def existencia_Art(matriz, columna, posicion):
    return matriz[columna][posicion]

# obtener_id
# matriz: la tabla en la que deseas encontrar el identificador
# indice: el indice del elemento del que deseas encontrar el identificador o -1 si el indice es incorrecto
def obtener_id(matriz, indice):
    if indice < len(matriz[0]) and indice >= -len(matriz[0]):
        return matriz[0][indice]
    else:
        return -1
# Abrir el archivo de productos, leer su informacion y carga la informacion en lista_productos
def cargarProductos():
    ruta_productos = Path('archivos', 'productos.csv')
    archivo_productos = open(ruta_productos)
    content_productos = archivo_productos.readlines()
    for line in content_productos:
        lista_productos.append(line.strip().split(','))
    archivo_productos.close()
    
    
#Abrir el archivo de producto y guarda en el la informacion que hay en lista_productos
def guardarProductos():
    string_content = ""
    for lines in lista_productos:
        for idx, element in enumerate(lines):
            if idx == len(lines) - 1:
                string_content += element + "\n"
            else:
                string_content += element + ","

    string_content = string_content.strip()
    ruta_productos = Path('archivos', 'productos.csv')
    archivo_productos = open(ruta_productos, "w")
    archivo_productos.write(string_content)
    archivo_productos.close()

def menu():
    print()
    print("  Elija una de las siguientes opciones:")
    print("    1. Registrar ventas")
    print("    2. Registrar artículos")
    print("    3. Consultar inventario")
    print("    4. Consultar ventas")
    print("    5. Reporte de ventas por vendedor")
    print("    6. Reporte de ventas por artículo")
    print("    0. Guardar y salir")
    return int(input(">> "))

def registrar_venta():
    print("Registra venta")
    
    nproducto  = (input("Ingrese el nombre del producto: ")).lower()
    producto = buscar_elemento(lista_productos, productos.SUB_MARCA, nproducto)
    while True:        
        vendedor = (input("Nombre del vendedor que atendió: ")).lower()             
        vendedorIdx = buscar_elemento(lista_vendedores, vendedores.NOMBRE, vendedor)
        if vendedorIdx != -1:
            break
        else:
            print(f"El vendedor {vendedor} no está registrado en el sistema.")
    maximo=(len(lista_productos[0]))-1
    if producto >= 0 and producto <= maximo:
        cantidad = int(input("¿Cuantos productos quiere?: "))
        existencia  = int(existencia_Art(lista_productos, 5, producto ))
        if existencia < cantidad:
            if existencia > 0:
                llegada = existencia_Art(lista_productos, 6, producto)
                print("Solo contamos con: ", + existencia) 
                print("Llegan nuevos el: " + llegada)
                confirmacion = int(input("Ingrese 1 si quiere realizar la compra, ingrese 2 si desea esperar: "))
                if confirmacion == 1:
                    precio = int(existencia_Art(lista_productos, 4, producto))
                    total = existencia*precio
                    lista_productos[5][producto]=str(existencia-existencia)
                    print("Su total es de: $",+total)                                          
                    if vendedorIdx != -1:
                        vendedorIdx += 1
                        lista_ventas[0].append(vendedorIdx)
                        lista_ventas[1].append(producto)
                        fecha = input("Ingrese la fecha de la venta en el formato M/D/A: ")
                        lista_ventas[2].append(fecha)
                        lista_ventas[3].append(existencia)
                        lista_ventas[4].append(total)
                        print("Venta registrada exitosamente")                       
                        
                else:
                    print("Que tenga una buena tarde, vuelva pronto.")
            else:
                llegada = existencia_Art(lista_productos, 6, producto)
                print("No hay en existencia, llegan nuevos el: " + llegada)
        else:
            precio = int(existencia_Art(lista_productos, 4, producto))
            total = cantidad*precio
            print("Su total es de: $",+total)
            lista_productos[5][producto]=str(existencia-cantidad)

            while True:
                vendedor = input("Nombre del vendedor que atendió: ")
                vendedorIdx = buscar_elemento(lista_vendedores, vendedores.NOMBRE, vendedor)
                if vendedorIdx != -1:
                    vendedorIdx += 1
                    lista_ventas[0].append(vendedorIdx)
                    lista_ventas[1].append(producto)
                    fecha = input("Ingrese la fecha de la venta en el formato M/D/A: ")
                    lista_ventas[2].append(fecha)
                    lista_ventas[3].append(cantidad)
                    lista_ventas[4].append(total)
                    print("Venta registrada exitosamente")
                    break
                else:
                    print(f"El vendedor {vendedor} no está registrado en el sistema.")
    else:
        print("Dicho articulo no se encuentra en el sistema")
  
def registar_articulo():
    print("Registra artículo")
    nproducto  = (input("Ingrese el nombre del producto: ")).lower()
    articulo = buscar_elemento(lista_productos, productos.SUB_MARCA, nproducto)
    maximo=len(lista_productos[0])-1 
    if articulo >= 0 and articulo <= maximo:
        existencia  = int(existencia_Art(lista_productos, 5, articulo ))
        cantidad = int(input("Cantidad de articulos a registrar: "))
        cant_nueva = cantidad + existencia
        lista_productos[5][articulo] = str(cant_nueva)
        print("Inventario actualizado exitosamente")
    else:
        print("Este es un articulo nuevo, ingrese los datos correctamente para registrarlo.")
        lista_productos[0].append(articulo)
        lista_productos[1].append(input('Ingrese la marca del producto: '))
        lista_productos[2].append(input('Ingrese la sub marca: '))
        lista_productos[3].append(input('Ingrese el modelo: '))
        lista_productos[4].append(input('Ingrese el precio por unidad: '))        
        lista_productos[5].append((input("Cantidad de articulos a registrar: ")))
        lista_productos[6].append('20/10/2021')
        print("Inventario actualizado exitosamente")

def consultar_inventario():
    print("Consulta inventario")
    while True:
        nproducto  = (input("Ingrese el nombre del producto: ")).lower()
        articulo = buscar_elemento(lista_productos, productos.SUB_MARCA, nproducto)
        maximo=len(lista_productos[0])-1
        llegada = existencia_Art(lista_productos, 6, articulo)
        if articulo >= 0 and articulo <= maximo:
            existencia  = int(existencia_Art(lista_productos, 5, articulo ))
            print(f"El articulo {nproducto} cuenta con {existencia} en existencia.")
            print(f"Se van a resurtir más el {llegada}.")
            break
        else:
            print("Este articulo no se encuentra en el inventario.")

def consultar_ventas():
    print_matriz(lista_ventas, ventas.COLUMNAS)
    print("Consulta venta")

def reporte_ventas_vendedor():
    print("Genera reporte")
    vendedor=input('¿Cual es el nombre del vendedor').lower()
    while True:
        vendedor_idx=buscar_elemento(lista_vendedores,vendedores.NOMBRE,vendedor)
        if vendedor_idx !=-1:
            break
        else:
            print(f'El nombre {vendedor.tittle()} no esta registrado')
    vendedor_id=buscar_elemento(lista_vendedores,vendedor_idx,vendedores.VENDEDOR_ID)
    rventas=[]
    for idx,id in enumerate (lista_ventas[ventas.VENDEDOR_ID]):
        if vendedor_id== id:
            rventas.append(idx)
    reporte_ventas=[[],[],[],[],[]]
    
    
    #for lista in rventas:
        
        #prdocto_id=lista_ventas[]





def reporte_ventas_articulo():
    print("Genera reporte")

def main():

    print("-" * 30)
    print("| Bienvenido a CompuTech |")
    print("-" * 30)
    cargarProductos()
    while True:
        selected = menu()
        if selected == 0:
            guardarProductos()
            print("Gracias por su visita")
            break
        elif selected == 1:
            registrar_venta()
        elif selected == 2:
            registar_articulo()
        elif selected == 3:
            consultar_inventario()
        elif selected == 4:
            consultar_ventas()
        elif selected == 5:
            reporte_ventas_vendedor()
        elif selected == 6:
            reporte_ventas_articulo()
        else:
            print(f"La opción {selected} no es válida")

main()  