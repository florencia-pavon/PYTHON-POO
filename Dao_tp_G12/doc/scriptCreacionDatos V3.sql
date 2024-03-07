--
-- Archivo generado con SQLiteStudio v3.4.3 el do. nov. 5 10:25:36 2023
--
-- Codificaci�n de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabla: estados
CREATE TABLE IF NOT EXISTS estados (estado_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, descripcion TEXT, activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo <= 1));
INSERT INTO estados (estado_id, descripcion, activo) VALUES (1, 'Disponible', 1);
INSERT INTO estados (estado_id, descripcion, activo) VALUES (2, 'Prestado', 1);
INSERT INTO estados (estado_id, descripcion, activo) VALUES (3, 'Extraviado', 1);

-- Tabla: libros
CREATE TABLE IF NOT EXISTS libros (libro_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, titulo TEXT NOT NULL, precio_reposicion NUMERIC (7, 2) NOT NULL, estado_id INTEGER REFERENCES estados (estado_id) NOT NULL, activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo <= 1));
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (1, 'Matematica I', 123, 2, 1);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (2, 'Matematica II', 123, 2, 1);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (3, 'Matematica I', 123, 2, 1);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (4, 'Lengua IV', 456, 2, 1);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (5, 'Lengua III', 456, 2, 1);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (6, 'Lengua III', 456, 2, 1);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (7, 'Sociales II', 789, 3, 0);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (8, '@TEST', 12.45, 1, 1);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (9, '@TEST BORRADO', 12.45, 3, 0);
INSERT INTO libros (libro_id, titulo, precio_reposicion, estado_id, activo) VALUES (10, '@TEST extravado', 12.45, 3, 0);

-- Tabla: prestamos
CREATE TABLE IF NOT EXISTS prestamos (prestamo_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, socio_id INTEGER REFERENCES socios (socio_id) NOT NULL, libro_id INTEGER REFERENCES libros (libro_id) NOT NULL, fecha_prestamo DATETIME NOT NULL, dias_pactados INTEGER NOT NULL CHECK (dias_pactados > 0), fecha_devolucion DATETIME, dias_retraso INTEGER CHECK (dias_retraso >= 0), activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo <= 1));
INSERT INTO prestamos (prestamo_id, socio_id, libro_id, fecha_prestamo, dias_pactados, fecha_devolucion, dias_retraso, activo) VALUES (1, 2, 3, '2023-10-20', 30, NULL, NULL, 1);
INSERT INTO prestamos (prestamo_id, socio_id, libro_id, fecha_prestamo, dias_pactados, fecha_devolucion, dias_retraso, activo) VALUES (2, 4, 1, '2023-10-21', 5, NULL, NULL, 1);
INSERT INTO prestamos (prestamo_id, socio_id, libro_id, fecha_prestamo, dias_pactados, fecha_devolucion, dias_retraso, activo) VALUES (3, 2, 6, '2023-10-25', 4, '2023-10-29', 0, 1);
INSERT INTO prestamos (prestamo_id, socio_id, libro_id, fecha_prestamo, dias_pactados, fecha_devolucion, dias_retraso, activo) VALUES (4, 3, 2, '2023-10-26', 1, NULL, NULL, 1);
INSERT INTO prestamos (prestamo_id, socio_id, libro_id, fecha_prestamo, dias_pactados, fecha_devolucion, dias_retraso, activo) VALUES (5, 3, 4, '2023-10-27', 2, NULL, NULL, 1);
INSERT INTO prestamos (prestamo_id, socio_id, libro_id, fecha_prestamo, dias_pactados, fecha_devolucion, dias_retraso, activo) VALUES (6, 3, 5, '2023-10-27', 4, NULL, NULL, 1);
INSERT INTO prestamos (prestamo_id, socio_id, libro_id, fecha_prestamo, dias_pactados, fecha_devolucion, dias_retraso, activo) VALUES (7, 2, 6, '2023-10-28', 4, '2023-10-28', 0, 0);




-- Tabla: socios
CREATE TABLE IF NOT EXISTS socios (socio_id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, apellido TEXT NOT NULL, nombre TEXT NOT NULL, email TEXT NOT NULL, celular TEXT NOT NULL, activo INTEGER DEFAULT (1) CHECK (activo >= 0 and activo <= 1));
INSERT INTO socios (socio_id, apellido, nombre, email, celular, activo) VALUES (1, 'Perez', 'Juan', 'jp@mail.com', '123456', 1);
INSERT INTO socios (socio_id, apellido, nombre, email, celular, activo) VALUES (2, 'Gonzalez', 'Maria', 'mg@mail.com', '456789', 1);
INSERT INTO socios (socio_id, apellido, nombre, email, celular, activo) VALUES (3, 'Castro', 'Marcos', 'cm@mail.com', '159753', 1);
INSERT INTO socios (socio_id, apellido, nombre, email, celular, activo) VALUES (4, 'Perez', 'Andrea', 'ap@mail.com', '951369', 1);
INSERT INTO socios (socio_id, apellido, nombre, email, celular, activo) VALUES (5, 'TEST Editar', ' Test', 'tt@mail.com', '9569', 1);
INSERT INTO socios (socio_id, apellido, nombre, email, celular, activo) VALUES (6, 'TEST Perez', 'BORRADO Andrea', 'ap@mail.com', '9569', 0);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
