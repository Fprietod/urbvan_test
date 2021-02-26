# Urbvan TEST 
## Data Engineer JR

[![N|Solid](https://cdn-images-1.medium.com/max/1200/1*7NVWswT3PWnDx9p99p_0ZA.png)](https://nodesource.com/products/nsolid)



Este repositorio cuenta con los diversos archivos que se utilizaron para poder resolver el test

- Códigos SQL
- Códigos python comentados y sin comentarios
- ✨Respuestas de los query del las respectivas preguntas
- Se han actualizado el script para insertar datos y crear la base de datos

## Códigos Python

- code_challenge_solutions.py
- problema1_con_comentarios.py
- problema_2_con_comentarios.py
- Script_insertar_csv.py
- sql_queries_urbvan.py

## Códigos SQL
- respuestas-query.sql

## Código Scala
- insert.scala


## Tecnologias adicionales utilizadas
- Amazon Web Services - RDS - PostgresSQL para la base de datos
- DBeaver -> Gestor para administrar la base de datos

A continuación se explicará brevemente en que consiste cada archivo, iniciamos con nuestros archivos python


| Python | Resumen |
| ------ | ------ |
| code_challenge_solutions.py | En este archivo se encuentra las soluciones a ambos problemas de manera general, se desarrollo usando una clase y sus respectivas funciones, basta con instanciar nuestro objeto y acceder a la función |
| problema1_con_comentarios.py | Este script es el desarrollo del primer problema del code challenge, sin embargo en este archivo se explica cada línea cual es su función y la lógica para resolver el problema |
| problema_2_con_comentarios.py |Este script es el desarrollo del segundo problema del code challenge, sin embargo en este archivo se explica cada línea cual es su función y la lógica para resolver el problema  |
| Script_insertar_csv.py | Este srcipt es el necesario para poder subir la información de cada csv en nuestra base de datos en postrgesSQL alojada en aws, se usaron las librerías de psycopg2 y obtenemos las funciones de create_table_queriesy drop_table_queries en este caso son una lista con las tablas que se deben crear y en este caso eliminar |
| sql_queries_urbvan.py | En este archivo se encuentra toda la estructura de las tablas que se crearon para la base de datos, tanto para crearlas, como eliminarlas |

## SQL y Scala

| SQL | Resumen |
| ------ | ------ |
| respuestas-query.sql | En este archivo se encuentran los querys que se utilizaron para poder las respectivas respuestas a las preguntas, cabe mencionar que se pueden optimizar estos querys, por el tiempo se opto por dejarlos como están |
| insert.scala | Este archivo es ideal utilizando Apache Zeppellin, similar como Jupyter, solo que este es para que podamos usar Spark, se intento configurar para poder subir los csv ya que por tiempos, para este caso de uso sería ideal utilizar spark para subir gran cantidad de archivos |




## AWS Endpoint
Si se desea comprobar que los registros se encuentran en la base de datos, el equipo puede comprobarlo accediendo a la base de datos que se encuentra en postgresSQL
| Endpoint | DB | Usuario | |Contraseña |
| ------ | ------ | --------------| --------| -----|
|database-2.c295zanvccq2.us-east-1.rds.amazonaws.com| urbvan|student||root2021|



## Créditos

Felipe Prieto de la Cruz

**Big Data!**
