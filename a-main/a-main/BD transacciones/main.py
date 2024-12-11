from BD.conexion import DAO
import VISTA.funciones
import matplotlib.pyplot as plt

dao=DAO()

def menuPrincipal():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Listar transacciones")
        print("2. Agregar Transaccion")
        print("3. Modificar transaccion")
        print("4. Resumen gasto mensual")
        print("5. Mostrar grafica de un mes")
        print("6. Finalizar")
        opc=int(input("Ingrese una opción (1-6): "))
        if opc<1 or opc>6:
            print("Opción inválida")
        elif opc==6:
            print("Hasta la vista")
            dao.cerrarConexion()
            break
        else:
            ejecutarOpcionMenu(opc)

def ejecutarOpcionMenu(opc):
    if opc==1:
        try:
            transacciones=dao.listarTransaccion()
            if len(transacciones) > 0:
                VISTA.funciones.listarTransaccion(transacciones)
            else:
                print("La tabla no tiene transacciones")
        except:
            print("Error.... ")
    elif opc==2:
        transacciones=VISTA.funciones.leerDatosTransaccion()
        try:
            dao.crearTransaccion(transacciones)
        except:
            print("Error.... ")
    elif opc == 3:
        id = VISTA.funciones.leerIdtransaccion()
        transaccion=dao.buscarTransacciones(id)
        if  transaccion!= None:
            transaccion=VISTA.funciones.leerDatosNuevosTransaccion(transaccion)
            dao.actualizarTransacciones(transaccion)
        else:
            print("Transaccion no Existe")
    elif opc==4:
        mes=input("Indique el numero del mes que desea buscar: ")
        print(dao.resumenMensual(mes))
        input("")

    elif opc==5:
        mes=input("Indique el numero del mes que desea buscar: ")
        transacciones=dao.buscarTodasTransacciones(mes)

        for monto in transacciones:
            print(int(monto))

        input("")

menuPrincipal()
