# Active X - BDOO

Sistema de gestión de un centro deportivo desarrollado con Python y ZODB.

## Descripción

Active X es un centro deportivo que ofrece diferentes actividades como:

- Gimnasio
- Natación
- Spinning
- Entrenamiento funcional
- Yoga

El sistema permite administrar usuarios, entrenadores, actividades,
clases, inscripciones, pagos y horarios.

## Rama actual
En esta rama se desarrollaron consultas relacionadas con las suscripciones del usuario,
tomando como parámetros id_usuario, id_clase y por su puesto root. Algunas de las funciones empleadas
fueron:

- inscripciones_activas_usuario
- cancelar_inscripcion
- inscripciones_canceladas_usuario
- historial_inscripciones

Estas consultas nos permiten conocer las clases en las que el usuario está inscrito, también nos
muestran aquellas suscripciones activas o canceladas. Estas últimas consultas están relacionadas 
el usuarios, es decir, no son búsquedas globales sino individuales. Al igual que el historial de
suscripciones. Solo nos interesa saber a qué clases está inscrito el usuario. 

Un caso interesante fue con la función inscripciones_canceladas_usuario, ya que para mostrar que 
realmente estaba ejerciendo sus funciones, se tuvo que crear otra función llamada cancelar_inscripcion.
Ya que hasta ese momento, todas la inscripciones estaban activas y el historial estaba vacío. 

Esto último ocasionó un problema que se creía lógico pero que no lo era. Ahora, la función cancelar_inscripcion,
inicialmente solo tomaba dos parámetros:

- root
- id_clase

Esto puede considerarse como un error de diseño, ya que si continuamos iterando, al final ningún usuario estará inscrito
en dicha clase. Por lo que se decidió aplicar otro parámetro que soluciona este error, y es el id_usuario. Suena más lógico
para la consulta y el programador decir el usuario quiere cancelar una clase en **específico** de las que él está inscrito. 
A diferencia de solo decir cancelar clase. 
## Tecnologías

- Python
- ZODB
- Git
- Visual Studio Code
- UML

## Estructura

```text
modelos/
persistencia/
servicios/
consultas/
main.py
README.md
requirements.txt
