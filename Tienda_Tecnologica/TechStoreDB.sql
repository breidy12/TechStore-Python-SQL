-- ================== SELECCIÓN DE BASE DE DATOS ==================
-- Indica que se trabajará sobre la base de datos Tienda_TecnologiaDB
USE Tienda_TecnologiaDB;
GO

-- ================== EJERCICIO 1: INNER JOIN ==================
-- Muestra los clientes junto con los productos que han comprado
SELECT 
    Clientes.Nombre AS NombreCliente,      -- Nombre del cliente
    Productos.Nombre AS NombreProducto,    -- Nombre del producto
    Productos.Precio AS PrecioProducto,    -- Precio del producto
    Productos.Cantidad AS CantidadProducto -- Cantidad del producto
FROM Clientes
INNER JOIN Productos 
    ON Clientes.Cedula = Productos.Cedula; -- Relación entre tablas
GO

-- ================== EJERCICIO 2: FUNCIÓN SUM ==================
-- Calcula el total de ventas sumando los precios de los productos
SELECT 
    SUM(Precio) AS TotalVentas
FROM Productos;
GO 

-- ================== EJERCICIO 3: FUNCIÓN AVG ==================
-- Calcula el precio promedio de todos los productos
SELECT 
    AVG(Precio) AS PrecioPromedio
FROM Productos;
GO

-- ================== EJERCICIO 4: FUNCIÓN COUNT ==================
-- Cuenta cuántos productos existen en la tabla Productos
SELECT 
    COUNT(*) AS TotalProductos
FROM Productos;
GO

-- ================== EJERCICIO 5: CREACIÓN DE VISTA ==================
-- Vista que muestra solo los productos con precio mayor a 1000
CREATE VIEW Vista_Productos_Caros AS
SELECT 
    Productos.Nombre AS NombreProducto,
    Productos.Precio AS PrecioProducto
FROM Productos
WHERE Productos.Precio > 1000;
GO

-- ================== EJERCICIO 6: PROCEDIMIENTO ALMACENADO ==================
-- Procedimiento que devuelve los productos de un cliente específico
CREATE PROC ObtenerProductosPorCliente
    @Cedula NVARCHAR(20) -- Parámetro de entrada
AS
BEGIN
    SET NOCOUNT ON;

    SELECT 
        Nombre AS NombreProducto,
        Precio AS PrecioProducto
    FROM Productos
    WHERE Cedula = @Cedula;
END;
GO

-- ================== EJERCICIO 7: UPDATE ==================
-- Actualiza el precio de un producto específico
UPDATE Productos
SET Precio = Precio * 1.10   -- Aumenta el precio en un 10%
WHERE Nombre = 'Laptop';
GO

-- ================== EJERCICIO 8: DELETE ==================
-- Elimina productos cuya cantidad sea cero
DELETE FROM Productos
WHERE Cantidad = 0;
GO

-- ================== EJERCICIO 9: GROUP BY ==================
-- Muestra el total de productos registrados por cada cliente
SELECT 
    Cedula,                          -- Cédula del cliente
    COUNT(*) AS CantidadProductos    -- Total de productos por cliente
FROM Productos
GROUP BY Cedula;
GO

-- ================== EJERCICIO 10: ORDER BY ==================
-- Muestra los productos ordenados del más caro al más barato
SELECT 
    Nombre AS NombreProducto,
    Precio AS PrecioProducto
FROM Productos
ORDER BY Precio DESC;
GO
-- ================== FIN DEL SCRIPT ==================