# monetal-django
<h1>Site Monetal em Django</h1>
<br/>
/monetal - diretório do projeto<br/>
/home - app home<br/>
/templates - arquivos de template<br/>
<br/>
<h3>Instalando o gunicorn</h3>

<strong>$ pip install gunicorn</strong><br/>
<br/>
Criar o arquivo de serviço:<br/>
<br/>
<strong>$ sudo vim /etc/systemd/system/[nome-do-site].service</strong>
<br/>
[code]<br/>
[Unit]<br/>
Description=gunicorn daemon<br/>
After=network.target<br/>
<br/>
[Service]<br/>
User=fabio<br/>
Group=www-data<br/>
WorkingDirectory=/home/fabio/projetos/monetal-django/<br/>
ExecStart=/home/fabio/projetos/monetal-django/p3env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/fabio/projetos/monetal-django/monetal.sock monetal.wsgi:application<br/>
<br/>
[Install]<br/>
WantedBy=multi-user.target<br/>
[/code]<br/>

<h3>Configurando o nginx</h3>

[code]<br/>
server {<br/>
    listen 80;<br/>
    server_name monetal;<br/>
<br/>
    #location = /favicon.ico { access_log off; log_not_found off; }<br/>
<br/>
    location /static/ {<br/>
	root /home/fabio/projetos/monetal-django/;<br/>
    }<br/>
<br/>
    location / {<br/>
        include proxy_params;<br/>
        proxy_pass http://unix:/home/fabio/projetos/monetal-django/monetal.sock;<br/>
    }<br/>
}<br/>
[/code]<br/>
