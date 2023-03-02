# 🕹️ pyGAMEcol
pyGAMECol es un sitio web desarrollado como proyecto final del Bootcamp de Backend con Python de [CódigoFacilito](https://codigofacilito.com/).

![Screenshot](https://github.com/sergiosano/pyGAMEcol/blob/main/static/img/demo.png)

# Descripción
pyGAMEcol permite mantener una colección simple de videojuegos.

Me gustaría decir que es un proyecto muy cuidado al que le he dedicado infinidad de horas, pero esa no es la verdad.

Como neófito total en el Bootcamp de Backend con Python, llegó un momento en el que me perdí, me desanimé y abandoné la idea de presentar ningún proyecto.

A poco más de una semana de la fecha final de entrega, algunos compañeros y profesores del Bootcamp me animaron a intentarlo...

Gracias a su motivación, a dormir menos unos cuantos días y a que mi bebé me mantuviera en vela algunas noches, este es el resultado de unas pocas noches de trabajo, sin tener apenas idea de Python y Django, y mucho menos de HTML y Bootstrap.

# Tecnologías
Entre otras, este sitio web utiliza tecnologías cómo:

- [Python](https://www.python.org/): Lenguaje de programación.
- [Django](https://www.djangoproject.com/): Framework web para Python.
- [MySQL](https://www.mysql.com/): Sistema de Gestión de Bases de Datos.

# Dependencias
- [asgiref v3.6.0](https://pypi.org/project/asgiref/3.6.0/)
- [Django v4.1.7](https://pypi.org/project/Django/4.1.7/)
- [mysqlclient v2.1.1](https://pypi.org/project/mysqlclient/2.1.1/)
- [Pillow v9.4.0](https://pypi.org/project/Pillow/9.4.0/)
- [python-decouple v3.7](https://pypi.org/project/python-decouple/3.7/)
- [sqlparse v0.4.3](https://pypi.org/project/sqlparse/0.4.3/)
- [tzdata v2022.7](https://pypi.org/project/tzdata/2022.7/)

# Puesta en marcha
- Descarga y descomprime o clona el repositorio en un directorio de tu PC.
- Dentro del directorio del proyecto, crea un entorno virtual: `python -m venv .venv`
- Activa el entorno virtual recién creado:
    - Linux/MAC: `source .venv/bin/activate`
    - Windows CMD: `.\.venv\Scripts\activate.bat`
    - Windows PowerShell: `.\.venv\Scripts\activate.ps1`
- Instala las dependencias del proyecto: `pip install -r requirements.txt`
- Por defecto, el proyecto usa SQLite como SGBD, para crear la base de datos:
    - Ejecuta las migraciones: `python manage.py migrate`
- En el caso de que desees utilizar otro SGBD: 
    - Edita el archivo `pyGAMEcol/settings.py`
    - Comenta la sección:

        ```
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': BASE_DIR / 'db.sqlite3',
            }
        }
        ```
    - Descomenta la sección:

        ```
        DATABASES = {
            'default': {
                'ENGINE': config('ENGINE'),
                'NAME': config('NAME'),
                'USER': config('USER'),
                'PASSWORD': config('PASSWORD'),
                'HOST': config('HOST'),
                'PORT': config('PORT'),
            }
        }
        ```
    - Crea un archivo `.env` en el directorio principal del proyecto con el siguiente formato (cambia el **ENGINE** y **PORT** si deseas trabajar con otro SGBD distinto a MySQL):
    
        ```
        ENGINE=django.db.backends.mysql
        NAME=pygamecol
        USER=usuario
        PASSWORD=contraseña
        HOST=host
        PORT=3306
        ```
    - Crea una base de datos nueva en la instancia del SGBD que estés utilizando, con el mismo nombre que el indicado en **NAME** del archivo `.env`
    - Ejecuta las migraciones: `python manage.py migrate`
- Crea un super usuario: `python manage.py createsuperuser`
- Ejecuta el servidor web integrado de Django: `python manage.py runserver`
- Al acceder pro primera vez al sitio web, se creará un usuario con datos de demostración, las credenciales son:
    - Usuario: **democol**
    - Contraseña: **democol23**