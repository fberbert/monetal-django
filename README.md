# monetal-django
<h1>Site Monetal em Django</h1>
<br/>
/monetal - diretório do projeto<br/>
/home - app home<br/>
/templates - arquivos de template<br/>
/static - arquivos estáticos<br/>
/config - arquivos de exemplo de configuração do gunicorn e nginx<br/>
<br/>

<h3>Preparando o ambiente</h3>

<strong>$ python3 -m venv p3env<br/>
$ source p3env/bin/activate<br/>
(p3env) $ pip install django</strong>
<br/><br/>

<h3>Configurando local_settings.py</h3>

Criar o arquivo monetal/local_settings.py com o seguinte conteúdo (ou mude suas configurações locais a seu gosto):
<br/><br/>

SECRET_KEY = 'cole-aqui-o-seu-hash'
DEBUG = True
ALLOWED_HOSTS = ['hostname-do-site']
<br/><br/>

<h3>Instalando o gunicorn</h3>

<strong>$ pip install gunicorn</strong><br/>
<br/>
Criar o arquivo de serviço:<br/>
<br/>
<strong>$ sudo vim /etc/systemd/system/[nome-do-site].service</strong>
<br/><br/>
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
<br/>
<strong>$ sudo service monetal start|stop|restart</strong>
<br/><br/>
<h3>Configurando o nginx</h3>

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
