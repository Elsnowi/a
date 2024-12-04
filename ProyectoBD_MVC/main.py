from BD.conexion import DAO
import VISTA.funciones

dao=DAO()

def menuPrincipal():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("1. Agregar Transaccion")
        print("2. Eliminar Transaccion")
        print("3. Crear Informe PDF")
        print("4. Finalizar")
        opc=int(input("Ingrese una opción (1-4): "))
        if opc<1 or opc>4:
            print("Opción inválida")
        elif opc==4:
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
            


menuPrincipal()

    

