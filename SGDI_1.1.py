# cambiar listas por diccionarios [X]
# cambiar las funciones para que usen dccionarios [x]




opcion=0
lista_productos=[]
#productos={"nombre": nombre ,"cantidad": stock, "precio":precio,}

def solicitar_produco():
    nombreProd= input("Ingrese el nombre del nuevo producto: ")
    try:
        precioProd= int(input("Ingrese el precio del nuevo producto: "))
        stockProd= int(input("Ingrese el stock del nuevo producto: "))
        if precioProd<0 or stockProd<0:
            raise ValueError
        else:
            return [nombreProd,precioProd,stockProd]
    except ValueError:
        print("Debe ingresar valores númericos positivos")

def buscarProducto(nombre):
    
    for producto in lista_productos : 
          if producto ["nombre"].lower() ==(nombre):
             return producto
          

def guardar_producto(nombre,precio,stock):

     if buscarProducto(nombre)== None :
         producto ={
              "nombre":nombre,
              "precio":precio,
              "stock":stock}
         lista_productos.append(producto)
         ("el producto se ha guardado con exito ")

     else: 
         print (" ya existe este producto con este nombre ")

def actualizarproduct(nombre,nuevoprecio,nuevostock):
    productobuscado=buscarProducto(nombre)
    if productobuscado!= None :
        indice=lista_productos.index(productobuscado)
        productobuscado["precio"]=nuevoprecio
        productobuscado["stock"]=nuevostock
        lista_productos[indice]=productobuscado
        print(f"se ha  actualizado el producto correctamente {productobuscado}")
    else: 
        print("el producto que se ha intentado actualizar no existe")

def mostrar_inventario ():

    for producto in lista_productos :
     print(f"Nombre: {producto}")

def eliminar_prod(nombre):
    productobuscado=buscarProducto(nombre)
    if productobuscado !=None:
     lista_productos.remove(productobuscado)
     print("producto eliminado correctamente ")



while opcion!="6":
    print("**************Menu de gestión de inventario**************")
    print("1.- Agregar producto")
    print("2.- Buscar producto")
    print("3.- Actualizar cantidad/precio")
    print("4.- Mostrar inventario completo")
    print("5.- Eliminar producto")
    print("6.- Salir")

    opcion= input("Ingrese la opción que desea(1-6): ")

    match opcion:
 
        case "1":
            infoproducto=solicitar_produco()
            if infoproducto !=None :
                guardar_producto(infoproducto[0],
                                 infoproducto[1],
                                 infoproducto[2])
        case "2":
            nombre=input("Ingrese el nombre del producto a buscar: ").lower()
            productoEncontrado=buscarProducto(nombre)
            if productoEncontrado!=None:
                print("_"*60)
                print(f"Nombre: {productoEncontrado["nombre"]} \t\t Precio: ${productoEncontrado["precio"]} \t\t Stock: {productoEncontrado["stock"]}")
                print("_"*60)
        case"3":
            actualiazar=actualizarproduct(nombre=infoproducto[0],nuevostock=infoproducto[1])
        case "4":
            mostrar_inventario()
        case "5":
            nombre=input("ingrese el nombre que quiere eliminar ").lower()
            eliminar_prod(nombre)