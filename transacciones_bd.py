import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="transacciones_financieras" 
)

cursor = db.cursor()

def agregar_transaccion(id,fecha, monto, tipo, descripcion):
    sql = "INSERT INTO transacciones (id,fecha, monto, tipo, descripcion) VALUES (%s, %s, %s, %s,%s)"
    val = (fecha, monto, tipo, descripcion)
    cursor.execute(sql, val)
    db.commit()
    print(f"Transacción agregada:{id}, {fecha}, {monto}, {tipo}, {descripcion}")

def obtener_transacciones():
    cursor.execute("SELECT * FROM transacciones")
    result = cursor.fetchall()
    for row in result:
        print(row)

def actualizar_transaccion(id, monto):
    sql = "UPDATE transacciones SET monto = %s WHERE id = %s"
    val = (monto, id)
    cursor.execute(sql, val)
    db.commit()
    print(f"Transacción con ID {id} actualizada")

def eliminar_transaccion(id):
    sql = "DELETE FROM transacciones WHERE id = %s"
    val = (id,)
    cursor.execute(sql, val)
    db.commit()
    print(f"Transacción con ID {id} eliminada")

def menu():
    print("*   MENU DE TRANSACCIONES *")
    print("* 1.-  Agregar transaccion *")
    print("* 2.- Actualizar transaccion *")
    print("* 3.- Eliminar transaccion  *")

agregar_transaccion(0,"2024-12-03", 150.75, "ingreso", "Pago por servicio")
#obtener_transacciones()
#actualizar_transaccion(1, 200.50)
#eliminar_transaccion(1)

cursor.close()
db.close()

