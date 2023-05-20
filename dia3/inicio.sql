--DDL( data definition lenguage)
--CREATE
--ALTER
--DROP
--TRUCANTE
--COMMENT
--RENAME
CREATE DATABASE prueba;

--creacion de la tabla alumnos
prueba=# CREATE TABLE alumnos(
prueba(# id serial NOT NULL PRIMARY KEY,
prueba(# nombre TEXT NOT NULL,
prueba(# apellido_paterno TEXT NULL,
prueba(# apellido_materno TEXT NULL,
prueba(# correo TEXT NOT NULL UNIQUE,
prueba(# fecha_nacimiento DATE,
prueba(# habilitado BOOLEAN DEFAULT true
prueba(# );

--DML-(data manipulation lenguaje)
--INSERT  insertar data a las tablas
--SELECT   seleccionar data de las tablas
--UPDATE  para actualizar la informacion contenida en las tablas
--DELETE  eliminar la informacion de la tabla

INSERT INTO alumnos(id, nombre, apellido_paterno, apellido_materno, correo, fecha_nacimiento, habilitado) VALUES 
(DEFAULT, 'Erick','Revoredo','Jiménez','erick.revoredo58@gmail.com','1994-10-22', DEFAULT);
--para poder ingresar varios registros de sentencia
INSERT INTO alumnos(id, nombre, apellido_paterno, apellido_materno, correo, fecha_nacimiento, habilitado) VALUES 
(DEFAULT, 'juan','silva','lopez','J.silva@gmail.com','1991-01-02', DEFAULT),
(DEFAULT, 'carlos','kishner','solorzano','c.kishner@gmail.com','1992-3-12', false),
(DEFAULT, 'johan','soldevilla','suarez','j.soldevilla@gmail.com','1994-11-01', DEFAULT),
(DEFAULT, 'brayan','mora','san martin','b.mora@gmail.com','1996-09-15', false);

--si queremos seleccionar toda la tabla
SELECT * FROM alumnos
SELECT * FROM alumnos WHERE nombre ='roxana','pedro' OR fecha_Nacimiento='roxana','pedro';

--el % sirve para que que busque  la letra "u" en cualquier ubicacion del nombre PERO SENsible a mayusculas y minusculas
SELECT nombre FROM alumnos WHERE nombre Like '%u%'

--devolver todos los alumnos con la letra "e" , pero no respetara si es mayuscula o minuscula.
SELECT nombre FROM alumnos WHERE nombre ILike '%u%'

--nos devolvera los nombres cuya segunda letra contenga la letra "0"
SELECT nombre FROM alumnos WHERE nombre ILike '_o%'

-- NOS devolvera los correos que contengan hotmail y gmail
SELECT *, correo FROM alumnos WHERE  correo ILIKE '%hotmail%' OR correo ILIKE '%gmail%'


CREATE TABLE direcciones (
    -- una columna llamada id que sea primary key y autoincrementable
    id  SERIAL PRIMARY KEY,
    -- calle  y tiene que ser text y no puede ser nula
    calle TEXT NOT NULL,
    -- numero numeral y no puede ser nulo
    numero INT NOT NULL,
    -- referencia tiene que ser text y puede ser nulo
    referencia TEXT NULL,
    -- alumno_id tiene que ser un numero y no puede ser nulo
    alumno_id INT NOT NULL,
    -- RELACIONES
    CONSTRAINT fk_direcciones_alumnos FOREIGN KEY(alumno_id) 
    REFERENCES alumnos(id)
);

INSERT INTO direcciones (id, calle, numero, referencia, alumno_id) VALUES
(DEFAULT, 'Av Ejercito', 1050, 'Al frente del Hospital', 1),
(DEFAULT, 'Av Tulipanes', 123, NULL, 1),
(DEFAULT, 'Calle Jose Olaya', 333, NULL, 2),
(DEFAULT, 'Giron Los Girasoles', 576, 'Al frente del parque', 3),
(DEFAULT, 'Pje. B', 8664, 'Al lado del periodiquero', 2),
(DEFAULT, 'Calle Los Martires', 123, NULL, 4),
(DEFAULT, 'Av Las condes', 252, 'En la esquina la casa blanca', 3);
--para poder visualizar columnas que sean nulas , se usa el operador IS  y no = para hacer uso de una asignacion
prueba=# SELECT * FROM direcciones  WHERE referencia IS NULL;
 id |       calle        | numero | referencia | alumno_id 
----+--------------------+--------+------------+-----------
  2 | Av Tulipanes       |    123 |            |         1
  3 | Calle Jose Olaya   |    333 |            |         2
  6 | Calle Los Martires |    123 |            |         4
(3 rows)

prueba=# SELECT * FROM direcciones  WHERE referencia IS NOT NULL;
 id |        calle        | numero |          referencia          | alumno_id 
----+---------------------+--------+------------------------------+-----------
  1 | Av Ejercito         |   1050 | Al frente del Hospital       |         1
  4 | Giron Los Girasoles |    576 | Al frente del parque         |         3
  5 | Pje. B              |   8664 | Al lado del periodiquero     |         2
  7 | Av Las condes       |    252 | En la esquina la casa blanca |         3
(4 rows)

-
SELECT* from direcciones WHERE (calle ILIKE 'AV%'  OR calle ILIKE 'calle%') AND referencia IS NULL;
--para hacer inner join juntar las 2 tablas
SELECT * FROM direcciones

INNER JOIN alumnos

ON direcciones.alumno_id = alumnos.id;