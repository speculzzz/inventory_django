#!/bin/bash

SSL_DIR="/etc/nginx/ssl"

mkdir -p "$SSL_DIR"

if [ ! -f "$SSL_DIR/localhost.crt" ] || [ ! -f "$SSL_DIR/localhost.key" ]; then
  openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout "$SSL_DIR/localhost.key" \
    -out "$SSL_DIR/localhost.crt" \
    -subj "/CN=localhost" -addext "subjectAltName=DNS:localhost,IP:127.0.0.1"
  echo "Self-signed certificates are generated in $SSL_DIR"
else
  echo "Certificates already exist, skip generation"
fi
