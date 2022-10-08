# no hay ENTRYPOINT porque el httpd hace de "entrypoint"
# mas info en https://hub.docker.com/_/httpd
FROM httpd:2.4
COPY ./website /usr/local/apache2/htdocs/
EXPOSE 80

#CMD arrancar servidor web