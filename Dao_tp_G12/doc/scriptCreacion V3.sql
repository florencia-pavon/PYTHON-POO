--
-- Archivo generado con SQLiteStudio v3.4.3 el do. nov. 5 10:25:36 2023
--
-- Codificación de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabla: estados
CREATE TABLE IF NOT EXISTS estados (estado_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, descripcion TEXT, activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo <= 1));

-- Tabla: libros
CREATE TABLE IF NOT EXISTS libros (libro_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, titulo TEXT NOT NULL, precio_reposicion NUMERIC (7, 2) NOT NULL, estado_id INTEGER REFERENCES estados (estado_id) NOT NULL, activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo <= 1));

-- Tabla: prestamos

-- Tabla: socios
CREATE TABLE IF NOT EXISTS socios (socio_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, apellido TEXT NOT NULL, nombre TEXT NOT NULL, email TEXT NOT NULL, celular TEXT NOT NULL, activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo <= 1));

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
