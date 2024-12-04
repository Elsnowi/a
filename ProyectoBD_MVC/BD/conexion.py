import mysql.connector
from mysql.connector import Error

class DAO():    # acrónimo de Data Access Object
    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',   # hosting
                port=3306,          # puerto de conexión
                user='root',        # usuario de MySql
                password='',    # contraseña de MySql
                db='transacciones_financieras'            # nombre de la BD
            )
        except Error as ex:
            print("Error de conexión: {0} ".format(ex))

    def listarTransaccion(self):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT *FROM transacciones ORDER BY fecha ")
                resultado=cursor.fetchall()
                return resultado
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))
        if (self.conexion.is_connected()):
            print("SI")
        else:
            print("NO")

    def crearTransaccion(self,transaccion):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                query="INSERT INTO transacciones (id,fecha,monto,tipo,descripcion) VALUES ({0},'{1}','{2}','{3}','{4}')"
                cursor.execute(query.format(0,transaccion[1],transaccion[2],transaccion[3],transaccion[4]))
                self.conexion.commit()
                print("Monto agregado exitosamente")
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def eliminarTransacciones(self,idEliminar):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                query="DELETE FROM transacciones WHERE id = {0}"
                cursor.execute(query.format(idEliminar))
                self.conexion.commit()
                print("transaccion eliminada exitosamente")
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def buscarTransacciones(self,id):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                cursor.execute("SELECT * FROM transacciones WHERE id = {0}".format(id))
                resultado=cursor.fetchone()
                return resultado
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def actualizarTransacciones(self,transaccion):
        if self.conexion.is_connected():
            try:
                cursor=self.conexion.cursor()
                query="UPDATE transacciones SET fecha='{1}',monto='{2}',tipo='{3}',descripcion={4}, WHERE id={0}"
                cursor.execute(query.format(transaccion[1],transaccion[2],transaccion[3],transaccion[4],transaccion[0]))
                self.conexion.commit()
                print("Persona actualizada correctamente")
            except Error as ex:
                print("Error de conexión: {0} ".format(ex))

    def cerrarConexion(self):
        if self.conexion.is_connected():
            self.conexion.close()
            print("Conexión cerrada exitosamente")
