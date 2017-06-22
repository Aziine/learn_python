import sqlite3 # imported sqlite module
connection sqlite3.connect("mycompany.db") # created empty database and connected to it

CREATE TABLE employee (
stuff_number INT NOT NULL AUTO_INCREMENT,
firstname VARCHAR (20),
lastname VARCHAR (30),
gender CHAR (1),
joining DATE,
birthdate DATE,
PRIMERY KEY (staff number) );
