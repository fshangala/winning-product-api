cp /data/winning-product-api/copiwinapi.service /etc/systemd/system/
systemctl daemon-reload
systemctl start copiwinapi
systemctl status copiwinapi