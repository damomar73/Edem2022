# APUNTES DE CONTENEDORES (DOCKER)

## VIRTUALIZACION
    Hacer creer a los SO que tenemOs muchas maquinas indenpedientes
    Dividir una maquina grande en muchas pequeñas con distinto SO
    Mas seguro ya que si atacan a una maquina no pueden a atacar a las otras al ser independientes
    Segun la carga de trabajo coges mas o menos maquinas y si baja dicha cargar puedes quitar maquinas
    Las maquinas virtuales consumen muchos recursos

DESKTOP VIRTUALIZATION  --> escritorio virtual
STORAGE VIRTUALIZATION --> dividir en partes el disco duro

HYPERVISOR --> visualizador de software, es el sw que crea las VM

## MAQUINAS VIRTUALES (VM)
Importante en que pais levantamos la maquina: influye velocidad o latencia, precio a pagar y seguridad de los datos
El precio varia segun la CPU y memoria escogidas de la VM
Igual que se importan VM se pueden exportar
A cada VM se asigna un HDD que es donde guardamos los datos
Si paramos la VM no cobran por ella pero si por el uso del HDD

## CI/CD
Ingenieria del software
Calidad del software
Desarrolladores --> GIT --> CIS (SERVIDOR DE INTEGRACION CONTINUA) --> Desarrolladores
DevOps --> integra infraestructuras y desarrollo

## ENTORNOS
 - Entorno de DESARROLLO: es local y es el PC donde programamos
 - Entorno de INTEGRACION: es donde subimos nuestros scripts junto con los del resto de desarrolladores
 - Entorno UAT (User Acceptance Testing): es donde se prueba los desarrollos por los usuarios 
 - Entorno de PRODUCCION: es el programa final que se lanza a todos los usuarios

## DOCKER
 - Es una forma de empaquetar
 - Se "levantan" contenedores no VM
 - Comparten SO con las VM 
    - eg: un contenedor de linux solo funciona en una VM de linux
 - Los contenedores no tienen SO, dependen de las VM
 - DOCKER DESKTOP --> levanta VM
 - No es un sustituto de las VM y es muy ligero

## DOCKER ENGINE
 - Si tecleamos en PC con windows "wsl" en la linea de comandos, se crea una VM en linux
    eg: wsl ls -l --> lista los archivos
 - Las imagenes NO se pueden modificar
 - Los contenedores SI se pueden modificar
 - Los cambios se guardan en el contenedor no en la imagen
 - Los contenedores se creean a partir de una imagen y puede existir conectividad entre contenedores
 - Cada vez que tecleamos "docker run" creamos un contenedor y pueden crearse varios con la misma imagen aunque seran distintos (diferente id)

## COMANDOS
 - docker run "id imagen" --> crea tantos contenedores como tantas veces lo ejecutes de la misma imagen pero NO entramos en el contenedor
 - docker run --name XXX id imagen --> creamos un contenedor llamado XXX con la imagen indicada
 - docker run -it "id imagen" --> creamos el contenedor y entramos en el si la imagen lo permite
 - docker run -d "id imagen" --> creamos el contenedor pero no secuestra la consola
 - docker rm "id container o nombre container" --> borra el contenedor con esa id o nombre
 - docker rmi "id imagen" --> borra la imagen con esa id
 - docker rm id id id --> borra los 3 contenedoers con dichas id
 - docker rmi id id id --> borra las 3 imagenes con dichas id
 - docker start "id container" --> arranca el contenedor que ya se habia creado
 - docker ps --> lista los contenedores en ejecucion
 - docker ps -a --> lista todos los contenedores incluso los que no se estan ejecutando
 - docker stop "id container" --> para el contenedor
 - docker start "id container" --> levanta el contenedor
 - docker start -i "id container" --> levanta el contenedor y se ejecuta, muestra por pantalla la ejecucion de la imagen, es "interactivo"
 - docker exec -it "id container" --> levanta el contenedor y puedo interactuar con el
 - docker image ls --> lista todas las imagenes
    - el TAG es la version de la imagen y "latest" significa la ultima version mas estable
    - es recomendable fijar la version ya que en caso de actualizacion no nos afecta
 - docker system prune --> borra todos los contenedores parados e imagenes sin nombre
 - clear --> limpia la pantalla 
 - exit --> salir del contenedor
 - en la linea de comandos root@XXXXXX--> el XXXXXX es la id del contenedor
 - docker run nginx --> crea un contenedor de la imagen nginx que "secuestra" la consola y espera interactuar con el usuario
 - docker inspect id imagen o id contenedor --> da info de la imagen o contenedor
 - docker top id container --> que procesos se estan desarrollando en el contenedor
 - docker stats id container --> ofrece estadisticas de consumo del contenedor
 - docker system df --> qofrece informacion del sistema
 - NO SE PUEDEN BORRAR LA IMAGENES QUE SE ESTAN USANDO EN UN CONTENEDOR
 - Contenedores en background --> estan vivos a nos ser que los paremos
 - docker run imagen comandos --> eg: docker run ubutu ls -l
 - docker cp souerce target:/ --> copia el archivo "source" en el contenedor "target" y en la ruta :/
 - en muchos contendores debemos indicar "bash" para poder ejecutarlos y entrar en ellos

 ## VOLUMENES & BIND MOUNTS
  - Volumenes: los gestiona docker. Carpeta en el servidor a la que docker tiene acceso
    - Volumenes anonimos: no se pueden compartir con otro contenedor al no tener nombre
    - Volumenes nominativos: pueden ser compartidos por contenedores
  - Bind mounts: los gestiona el SO

 - RUN: crea el contenedor
 - START: arranca un contenedor ya creado
 - EXEC: permite interactuar con un contenedor activo ya creado

 ### esto hay que revisarlo*************************************
 - docker run -it -v data:/data-in ubuntu --> la "-v" hace que copie la carpeta data_in en el contenedor ubuntu
 - docker run -it -v /data:/data-in ubuntu --> es los mismo pero no crea volumenes ya que empieza por /

 ## DOCKERFILE
  - el orden en que esta escrito es muy importante
  - cada comando es una capa
  - docker build . --> crea una imagen del dockerfile, importente estar en la misma carpeta y el archivo SIEMPRE debe llamarse "dockerfile"
  - docker build -t "nombre" . --> crea una imagen que se llama "nombre"
   

  






