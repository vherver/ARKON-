# Examen para desarrollador python.

_Proyecto para evaluacion de posición desarrollador python, el sistema se divide en las siguientes aplicaciones_

* Metrobus. Realiza las tareas necesarias para las tareas relacionadas con las lectura de informacion proveniente
del api de metrobus.

## Comenzando 

_Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu 
máquina local para propósitos de desarrollo_


### Pre-requisitos 

_Se utilizara Docker como herramienta para correr la aplicacion, por lo que será necesario contar con docker_


### Instalación 

_Una vez instalado docker y el repositorio en su maquina local debera ejecutar el en linea de comandos en la
raiz de este proyecto el comando docker-compose up, lo cual realizara las descargas necesarias de las imagenes y 
las dependencias requeridas por el proyecto._

_Una vez levantado el servidor la aplicacion correra en el puerto 8000_

## Recomendaciones

* Al realizar deploy en ambiente productivo será necesario cambiar la base de datos

## Importante

* SECRET_KEY deberá ser colocada como variable de ambiente en produccion para dejarla fuera
del archivo settings

* DJANGO_SETTINGS_MODULE en produccion deberá ser colocada como variable de ambiente con el
valor podemosExam.settings.prod

## Autores 

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Victor Hugo Herver Segura** - *Trabajo Inicial* - [VictorHerver](https://github.com/VictorHerver)  - [vicherver](https://gitlab.com/vicherver)


