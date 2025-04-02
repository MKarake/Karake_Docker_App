#  Use the official Nginx image from docker hub
FROM nginx:latest

#Every Nginx image comes with a default config , here we are replacing it with own own custom rules (from your nginx.conf)
COPY nginx.conf /etc/nginx/conf.d/default.conf

#  Copy frontend files into Nginx's root directory
#Nginx uses /usr/share/nginx/html/ as the folder to serve static files (like your site)
COPY public /usr/share/nginx/html/

#  it just marks that your app is listening on port 80
#Docker Compose will use this info when routing traffic
EXPOSE 80

#  This is the command that runs when the container starts
#nginx → starts the web server
#-g "daemon off;" → tells Nginx: "Don’t run in the background, stay in the foreground"
CMD ["nginx", "-g", "daemon off;"]
