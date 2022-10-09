# FUNDAMENTOS LINUX
## Información
    •	El Linux/Unix/Mac los programas se instalan siempre en la misma ubicación
    •	En Microsoft los programas se instalan cada vez en una ubicación (hay que averiguar dónde)
    •	Por defecto somos “root”, es decir, superusuarios
    •	Cheat sheet unix (búsqueda en Google para encontrar comandos de unix)
## Crear una maquina Linux
    •	Simulador online de sistemas operativos (interfaz de entorno Linux)
        o	https://bellard.org/jslinux/

    aqui va una tabla**********************
        CPU	OS	User Interface	VFsync access
Startup Link	TEMU Config

    x86	Alpine Linux 3.12.0	Console	Yes	click here
url


    •	Directorio raíz (/): el nodo más alto de la jerarquía también llamado root
    •	Directorio conexión (~): donde estamos cuando nos conectamos a la maquina
    •	Directorio trabajo (.): donde estamos trabajando en cada momento

## 1 -Creación imagen Linux en nuestro docker local

    Antes hay que abrir el programa “Docker desktop”!!!! (se puede comprobar si está abierto tecleando docker ps)

    •	docker create -it --name unix ubuntu:latest		crea un contenedor
    •	docker start unix					arranca el contenedor
    •	docker exec -it unix /bin/bash

    Los archivos con extension . bin son archivos binarios. Todos los ejecutables están en la carpeta “bin”

    Suelen ser instaladores de programas y tienen la ventaja de que funcionan en la mayoría de distribuciones, es un formato de archivo comprimido que puede contener en su interior información como imágenes y vídeos, y que muchas aplicaciones utilizan para diversos fines.

## 2- Instalar java

    •	apt update--> actualiza repositorios
        o	sudo apt update --> sudo te hace superusuario
    •	apt install openjdk -8-jdk --> instala java en nuestro contenedor
        o	apt install --> para instalar siempre ya sea java, git u otro programa
    •	crear un fichero script
        o	touch script.sh
        o	todos los ficheros script deben comenzar con la línea:
            	#!/bin/bash --> indica que es un fichero que debe ejecutar
    •	Para ello tecleamos eco ‘#!/bin/bash’
        o	. ./script.sh --> ejecuta el script
    •	exit --> salimos del Docker



## COMANDOS
    •	ls --> listar archivos y carpetas
        o	ls *.pdf --> lista todos los archivos .pdf
        o	ls -l --> ver detalles archivos
        o	ls -lt --> archivos ordenados por tiempo
        o	ls -ltr --> archivos ordenados por tiempo de forma inversa
        o	ls -l *.pdf --> lista detalles de todos los archivos .pdf

    •	touch --> crear ficheros
        o	touch hola.txt --> crea fichero hola.txt)
        o	touch Ej1/primero.txt --> crea el fichero “primero.txt” en carpeta Ej1) --> ruta relativa
        o	touch /usr/hola.txt --> crea fichero “hola.txt” en carpeta usr pero primero va a la raíz --> ruta absoluta
        o	touch hola1.txt hola2.txt hola3.txt --> crea 3 archivos a la vez, hola1, hola2 y hola 3

    •	cat --> mostrar lo que contiene los archivos
        o	cat hola.txt --> muestra el contenido del archivo hola.txt

    •	echo --> escribir
        o	echo hola --> escribe “hola”
        o	echo hola a todos > hola.txt --> escribe “hola a todos” en fichero hola.txt
        o	echo yyy > hola.txt --> si no existe el fichero hola.txt, lo crea y escribe “yyy”
        o	echo adios >> hola.txt --> concatena “adios” a lo que ya hay escrito en hola.txt, es decir añade

    •	rm --> borrar
        o	rm hola.txt --> borra el fichero hola.txt
        o	rm -r --> borra todos los archivos de la carpeta, “podo el árbol”
        o	rm -rf YYYY --> borra la carpeta YYYY y todo su contenido

    •	mv --> mover
        o	mv /usr/hola.txt . --> mueve hola.txt de user a donde me encuentro ahora, la clave es el .
        o	mv *.txt /usr/ --> mueve todos los archivos .txt a la carpeta user --> ruta absoluta
        o	mv *.txt curso --> mueve todos los ficheros .txt a carpeta curso --> ruta relativa
        o	mv DIR1/Ej1/hola.txt DIR1/Ej2 --> mueve “hola.txt” de Ej1 a Ej2 --> ruta relativa

    •	cp --> copiar
        o	cp hola.txt adios.txt --> copia el contenido de hola.txt en el fichero adios.txt, crea un fichero con el mismo contenido pero nombre distinto
    •	hola.txt es el origen
    •	adios.txt es el destino
        o	cp Remember/Ej1/hola.txt Remember/Ej2 --> copia “hola.txt” de Ej1 a Ej2

    •	mkdir --> crea un directorio con el nombre y la ruta que se especifique. Si no se indica    ninguna ruta, por defecto, creará la carpeta dentro del directorio de trabajo en el que nos encontremos
        o	mkdir ~/Ejercicio --> crea la carpeta “Ejercicio” en nuestro directorio de trabajo

    •  	pwd --> indica donde te encuentras

    •	cd --> cambiar de directorio o carpeta
        o	cd XXXXX --> cambia a la carpeta XXXXX
        o	cd / --> vas a la raíz
        o	cd /user/bin --> vamos a user y luego bin
        o	cd .. --> subes a un nivel superior de carpeta
    •	help XXX o man XXX --> informacion del comando XXX
    •	df --> info capacidad del disco duro
        o	df -h --> info capacidad del disco duro en gigas
    •	apt install --> instalar

## Comando/parámetro/argumento
    •	ls - FFFFF
        o	ls es el comando
        o	lo que va seguido de – es el parámetro (siempre seguido de -)
        o	FFFF es el argumento
        o	No siempre tiene porque haber parámetros o argumentos con un comando, hay comandos que solo llevan argumentos o que solo llevan parámetros 
    •	ls -l *.c
        o	ls	comando
        o	-l	parametro
        o	*.c	argumemto

## Rutas
    •	Ruta absoluta	(usamos /)  da igual donde estemos, al dar toda la ruta desde la raíz, es siempre igual
    •	Ruta relativa	(no usamos /)   parte desde donde nos encontramos, si cambiamos de carpeta varia la ruta

## Directorios
    •	Directorio raíz (ej. Portal finca)
        o	cd /
    •	Directorio conexión (donde estamos al entrar a linux, punto de entrada, ej. puerta casa)
        o	cd  ~ (alt + 126 o altGr+4)
    •	Directorio de trabajo (donde estamos en cada ocasión)
        o	cd .

## Permisos
    •	chmod --> cambiar permisos de ficheros
        •	r	leer
        •	w	escribir
        •	x	ejecutable
            o	chmod 440 hola.txt --> cambia los permisos de hola.txt, 440 es el código de seguridad
            o	chmod 777 hola.txt --> da todos los permisos a todos del archivo hola.txt

            
AQUI VA UNA IMAGEN********************

## Contenido del ejercicio Unix resuelto hecho en clase como Script.sh:

    !#/bin/bash
        La primera línea le dice a Unix qué tipo de interprete vamos a utilizar

    Crear carpeta
        mkdir EjercicioRemember

    Dentro de EjercicioRemember crear Ej1 y Ej2
    opcion A
        mkdir EjercicioRemember/Ej1
        mkdir EjercicioRemember/Ej2

    En ej1 crear un fichero primero.txt con permiso de lectura para el grupo solo
        touch EjercicioRemember/Ej1/primero.txt
        chmod 040 EjercicioRemember/Ej1/primero.txt

    En ej2 crear un fichero Segundo.txt con todos los permisos
        touch EjercicioRemember/Ej2/segundo.txt
        chmod 777 EjercicioRemember/Ej2/segundo.txt

    Copiad primero.txt a ej2 y moved Segundo.txt a ej1
        cp EjercicioRemember/Ej1/primero.txt EjercicioRemember/Ej2
        mv EjercicioRemember/Ej2/segundo.txt EjercicioRemember/Ej1

    Listar el contenido de ej1
        ls EjercicioRemember/Ej1

    Escribir en primero.txt “El Data mola mogollón”
        echo “El Data mola mogollón” > EjercicioRemember/Ej1/primero.txt

    Mostrar el contenido de primero.txt
        cat EjercicioRemember/Ej1/primero.txt
