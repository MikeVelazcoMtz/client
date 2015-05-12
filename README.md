# Instalación del proyecto: Clientes

La instalación inicia con la [clonación del proyecto](https://github.com/MikeVelazcoMtz/client.git)

~~~
git clone https://github.com/MikeVelazcoMtz/client.git
~~~

Crear un virtualenv (desde virtualenvwrapper) llamado clientes:

~~~
mkvirtualenv client
~~~

Realizar la instalación de los paquetes adicionales dentro del repositorio:

~~~
pip install -r requirements.txt
~~~

Entrar a la consola de MySQL y crear la base de datos 'clientes':

~~~
$ mysql -uroot
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 1
Server version: 5.6.21 Homebrew

Copyright (c) 2000, 2014, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> create database clientes;
Query OK, 1 row affected (0,04 sec)

mysql> exit;
Bye
~~~

A continuación ejecutamos `makemigrations`:

~~~
$ python manage.py makemigrations
No changes detected
~~~

y `migrate`:

~~~
$ python manage.py migrate
Operations to perform:
  Synchronize unmigrated apps: clientes
  Apply all migrations: admin, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
  Installing custom SQL...
  Installing indexes...
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying sessions.0001_initial... OK
~~~

Para terminar, creamos el usuario `root`:

~~~
$ ./manage.py syncdb
Operations to perform:
  Synchronize unmigrated apps: clientes, bootstrap3
  Apply all migrations: admin, contenttypes, auth, sessions
Synchronizing apps without migrations:
  Creating tables...
  Installing custom SQL...
  Installing indexes...
Running migrations:
  No migrations to apply.

You have installed Django's auth system, and don't have any superusers defined.
Would you like to create one now? (yes/no): yes
Username (leave blank to use 'usuario'): root
Email address:
Password:
Password (again):
Superuser created successfully.
~~~

Iniciar el servidor:

~~~
$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
May 11, 2015 - 17:21:23
Django version 1.7.1, using settings 'clientes.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
~~~

Ahora solamente queda mostrar el template [base.html](http://127.0.0.1:8000/).

![base.html](http://s30.postimg.org/3vrrlbrrl/Captura_de_pantalla_2015_05_11_a_las_13_19_29.png)

>##Nota:
>La implementación de [Bootstrap](http://getbootstrap.com) es realizada por medio del plugin [Django-bootstrap3](https://github.com/dyve/django-bootstrap3) la documentación esta ([aquí](http://django-bootstrap3.readthedocs.org/))
>
>El archivo requirements.txt incluye bpython para ayudar al momento de probar código.
>
>La versión de Django es 1.7.1.
