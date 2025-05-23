# Dockerfile
FROM nginx:alpine

# Copy static HTML, CSS, JS to nginx default public folder
COPY . /usr/share/nginx/html

# Replace default nginx config
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
