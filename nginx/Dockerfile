FROM nginx:1.21

COPY scripts/generate-ssl.sh /docker-entrypoint.d/

RUN chmod +x /docker-entrypoint.d/generate-ssl.sh

COPY nginx.conf /etc/nginx/conf.d/default.conf
