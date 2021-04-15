FROM nginx
COPY ./secrets /secrets
COPY ./reverse.conf /etc/nginx/conf.d
ENTRYPOINT nginx -g 'daemon off;'