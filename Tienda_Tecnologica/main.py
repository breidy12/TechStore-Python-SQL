# ================== IMPORTACIÓN DE LIBRERÍAS ==================

# Pandas se utiliza para manejar datos en forma de tablas (DataFrame)
# y para exportar información a archivos Excel
import pandas as pd

# pyodbc se utiliza para conectarse a SQL Server desde Python
import pyodbc


# ================== CONEXIÓN A LA BASE DE DATOS ==================

# Se establece la conexión con SQL Server
# Driver: controlador de SQL Server
# Server: nombre del servidor
# Database: base de datos a utilizar
# Trusted_Connection: usa la autenticación de Windows
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-K8L48DR;'
    'Database=Tienda_TecnologiaDB;'
    'Trusted_Connection=yes;'
)

# Se crea el cursor que permite ejecutar sentencias SQL
cursor = conn.cursor()


# ================== MENSAJE DE BIENVENIDA ==================

print("\n¡Bienvenido a la Tienda Tecnológica en Python!\n")


# ================== CONSULTA DE DATOS DESDE SQL SERVER ==================

# Se obtienen todos los registros de la tabla Productos
df_productos = pd.read_sql("SELECT * FROM Productos", conn)

# Se obtienen todos los registros de la tabla Clientes
df_clientes = pd.read_sql("SELECT * FROM Clientes", conn)

# ================== EXPORTAR DATOS A EXCEL ==================

# Se crea un archivo Excel con dos hojas:
# - Productos
# - Clientes
with pd.ExcelWriter('Inventario_Tienda_Tecnologia.xlsx') as writer:
    
    # Se exporta la tabla Productos a una hoja llamada "Productos"
    df_productos.to_excel(writer, sheet_name='Productos', index=False)
    
    # Se exporta la tabla Clientes a una hoja llamada "Clientes"
    df_clientes.to_excel(writer, sheet_name='Clientes', index=False)

# Se confirman cambios en la base de datos (aunque aquí solo se leen datos)
conn.commit()

print("Archivo Guardado: Inventario_Tienda_Tecnologia.xlsx\n")


# ================== INGRESO DE DATOS DEL CLIENTE ==================

print("=== DATOS PERSONALES ===\n")

# Se solicitan los datos del cliente por consola
cedula = input("Cédula: ")
nombre = input("Nombre completo: ")
direccion = input("Dirección: ")
telefono = input("Teléfono: ")
correo = input("Correo electrónico: ")


# ================== INSERCIÓN DEL CLIENTE EN LA BD ==================

# Se inserta el cliente en la tabla Clientes usando parámetros
# para evitar inyección SQL
cursor.execute("""
    INSERT INTO Clientes (Cedula, Nombre, Email, Telefono, Direccion)
    VALUES (?, ?, ?, ?, ?)
""", (cedula, nombre, correo, telefono, direccion))

# Se guardan los cambios en la base de datos
conn.commit()

print("\nCliente registrado correctamente.\n")


# ================== REGISTRO DE PRODUCTOS ==================

# Lista para guardar los productos agregados (uso interno)
productos = []

# Bucle para permitir agregar múltiples productos
while True:
    print("\n=== AGREGAR PRODUCTO ===\n")

    # Se solicitan los datos del producto
    id_producto = input("ID del producto: ")
    nombre_producto = input("Nombre del producto: ")
    categoria = input("Categoría: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad: "))

    # Se inserta el producto en la tabla Productos
    cursor.execute("""
        INSERT INTO Productos (ProductoID, Nombre, Precio, Cantidad, Categoria, Cedula)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (id_producto, nombre_producto, precio, cantidad, categoria, cedula))

    # Se confirman los cambios en la base de datos
    conn.commit()

    print("\nProducto agregado correctamente.\n")

    # Se guarda el producto en una lista para un posible resumen
    productos.append({
        "ID Producto": id_producto,
        "Producto": nombre_producto,
        "Categoria": categoria,
        "Precio": precio,
        "Cantidad": cantidad,
        "Total": precio * cantidad
    })

    # Se pregunta si desea agregar otro producto
    continuar = input("\n¿Agregar otro producto? (s/n): ")
    
    # Si la respuesta no es 's', se sale del bucle
    if continuar.lower() != 's':
        break


# ================== RESUMEN DE PRODUCTOS ==================

# Se crea un DataFrame con los productos agregados
df = pd.DataFrame(productos)

print("\nGracias por su compra. ¡Esperamos verlo de nuevo pronto!\n")


# ================== CIERRE DE CONEXIÓN ==================

# Se cierra el cursor
cursor.close()

# Se cierra la conexión con la base de datos
conn.close()