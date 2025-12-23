🛒 TechStore – Python & SQL Server
Sistema de gestión para una tienda tecnológica desarrollado con Python, SQL Server y Excel, que permite registrar clientes, administrar productos, realizar consultas SQL avanzadas y exportar información a archivos Excel.

Este proyecto integra programación, bases de datos y análisis de datos, ideal como proyecto académico o de portafolio profesional.

📌 Características principales
Conexión a SQL Server usando pyodbc

Registro de clientes desde consola

Registro de múltiples productos asociados a un cliente

Inserción segura de datos (prevención de SQL Injection)

Consultas SQL avanzadas:

JOIN

SUM, AVG, COUNT

GROUP BY, ORDER BY

VIEWS

STORED PROCEDURES

UPDATE y DELETE

Exportación de datos a Excel con pandas

Código comentado y estructurado

TechStore-Python-SQL/
│
├── main.py
├── TechStoreDB.sql
├── Inventario_Tienda_Tecnologia.xlsx
├── README.md

🛠️ Tecnologías utilizadas
Python 3

SQL Server

pandas

pyodbc

Excel

📂 Descripción de archivos
🔹 main.py
Aplicación principal en Python que:

Se conecta a SQL Server

Consulta clientes y productos

Exporta datos a Excel

Permite registrar clientes

Permite agregar múltiples productos por cliente

🔹 TechStoreDB.sql
Script SQL que incluye:

Consultas con INNER JOIN

Funciones agregadas (SUM, AVG, COUNT)

Creación de vistas

Procedimientos almacenados

Operaciones UPDATE y DELETE

Agrupaciones y ordenamientos

🔹 Inventario_Tienda_Tecnologia.xlsx
Archivo Excel generado automáticamente que contiene:

Hoja Productos

Hoja Clientes

▶️ Cómo ejecutar el proyecto
git clone https://github.com/tu-usuario/TechStore-Python-SQL.git
pip install pandas pyodbc

Asegúrate de tener:

SQL Server instalado

La base de datos Tienda_TecnologiaDB creada

Las tablas Clientes y Productos

Ejecuta el programa:
python main.py

⚠️ Nota importante
Antes de ejecutar el proyecto, ajusta los datos de conexión en main.py:

Server=DESKTOP-K8L48DR;
Database=Tienda_TecnologiaDB;
Cambia el nombre del servidor si es necesario.

🎯 Objetivo del proyecto
Este proyecto fue desarrollado con fines:

Educativos

Práctica de Python y SQL Server

Demostración de habilidades para portafolio
