def listarTransaccion(transaccion):
    print("\nNómina de transacciones\n")
    c=1
    for tra in transaccion:
        datos="Id: {0}. Fecha: {1} │ Monto: {2} │ Tipo: {3} │ Descripcion: {4} "
        print(datos.format(tra[0],tra[1],tra[2],tra[3],tra[4]))
        c+=1
    print("")

def leerDatosTransaccion():
    # Falta validar datos >> TAREA
    id=int(input("Id: "))
    fecha=input("Fecha (formato dia/mes/año): ")
    monto=int(input("Monto: "))
    tipo=input("Tipo: ")
    descripcion=input("Descripcion: ")
    transaccion=(id,fecha,monto,tipo,descripcion)
    return transaccion

def leerIdtransaccion():
    return int(input("Id transaccion a buscar: "))

def leerDatosNuevosTransaccion(transaccion):
    id=transaccion[0]
    fecha = transaccion[1]
    monto = transaccion[2]
    tipo = transaccion[3]
    descripcion = transaccion[4]
    print(transaccion)
    while True:
        print("Id: ",id)
        print("1. Modifica Fecha: ",fecha)
        print("2. Modifica Monto: ",monto)
        print("3. Modifica Tipo: ",tipo)
        print("4. Modifica Descripcion: ",descripcion)
        print("5. Retornar")
        opc=int(input("Opción (1-6): "))
        if opc==1:
            fecha=input("Nueva fecha")
        elif opc==2:
            monto=input("Monto: ")
        elif opc==3:
            tipo=input("Tipo: ")
        elif opc==4:
            descripcion=int(input("Descripcion: "))
        else:
            transaccion=(id,fecha,monto,tipo,descripcion,)
            break
    return transaccion

