# creando la lista vacia
listaRegistro = []

clientes = 0
ventasTotales = 0.0
respuesta = "si"
while respuesta == "si":
    cliente = input("nombre del cliente: ")
    producto = input("producto: ")
    costo = float(input("costo ($0.00): "))
    ventasTotales += costo
    # punto programa
    # registro = {"cliente": cliente, "producto": producto, "costo": costo)
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    # como agrego un elemento nuevo a una lista?
    listaRegistro.append(registro)
    # dejar de ocupar la variable registro
    # registro = None
    respuesta = input("Desea ingresar otro cliente? (Responde): ")

print("El dia ha finalizado")
print("Ventas Totales: " + str(ventasTotales))
