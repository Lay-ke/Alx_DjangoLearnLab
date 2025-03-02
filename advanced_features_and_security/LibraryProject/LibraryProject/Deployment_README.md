## Deploying with HTTPS

To make sure these settings(Security settings in settings.py) work in production, you'll need to serve your Django application over HTTPS. If you're using a web server like Nginx or Apache, ensure that they are configured to handle HTTPS requests and that SSL certificates are correctly set up.

For example, in Nginx, you would configure it to listen on port 443 (HTTPS) and redirect traffic from HTTP to HTTPS.

### Example Nginx Configuration:

```nginx
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;

    ssl_certificate /path/to/your/certificate.crt;
    ssl_certificate_key /path/to/your/private.key;
    # Additional SSL configurations
}
```