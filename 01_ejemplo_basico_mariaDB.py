import mysql.connector
# configuracion de la base de datos
config = {
    'user':'root',
    'password':'',
    'host':'localhost',
    'database':'empresadb'
}
# creamos conexion a la base de datos
try:
    conexion = mysql.connector.connect(**config)
    if conexion.is_connected():
        print('Conectado a mariaDB')
except mysql.connector.Error as e:
    print('Error al conectar a mariaDB',e)
finally:
    if conexion in locals():
        conexion.close()
        print('Conexion cerrada')
def conectar():
    try:
        return mysql.connector.connect(**config)
    except mysql.connector.Error as e:
        return False
def cerrar_conexion(conexion):
    if conexion in locals():
        conexion.close()
        print('Conexion cerrada')  
        return True      
# creamos tabla
conexion = conectar()
cursor = conexion.cursor()
crear_tabla_query = '''CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    email VARCHAR(100) NOT NULL
    )'''
cursor.execute(crear_tabla_query)
# insertar datos
insertar_query = "INSERT INTO usuarios (nombre, email) VALUES (%s, %s)"
dato = ("Pedro","k65djaf@gmail.com")
cursor.execute(insertar_query, dato)
dato = ("Maria","k56ddafjaf@gmail.com")
cursor.execute(insertar_query, dato)
conexion.commit()
# actualizar datos
actualizar_query = "UPDATE usuarios SET nombre = %s WHERE id = %s"
dato = ('Antonio',4)
cursor.execute(actualizar_query, dato)
conexion.commit()
# borrar datos
borrar_query = "DELETE FROM usuarios WHERE nombre = %s"
dato = ("Alberto",)
cursor.execute(borrar_query, dato)
conexion.commit()
# consulta datos
consulta_query = "SELECT * FROM usuarios"
cursor.execute(consulta_query)
resultado = cursor.fetchall()
for registro in resultado:
    print(registro)
cerrar_conexion(conexion)
    




