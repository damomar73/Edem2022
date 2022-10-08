# Ejercicio 9 (pagina 38)
# se ejecuta con docker image
FROM ubuntu:20.04

RUN apt-get update
RUN apt-get install -y git

# se ejecuta con docker run
# se podia haber ejecutado con CMD [" "] o con ENTRYPOINT
#ENTRYPOINT git --version
CMD git --version