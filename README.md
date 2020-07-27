# Vision Artifical
## Descripcion de proyecto
Una persona ciega o con visión limitada, en algún momento de su vida requerirá de asistencia visual, sin embargo el grave problema al que tarde o temprano se deberán enfrentar es el de encontrarse sin asistencia alguna. Nuestro proyecto pretende ayudar a estas personas en esta difícil situación.

Nuestro proyecto se presenta como: Un mundo hecho con palabras. El objetivo de este proyecto es ver cómo la tecnología puede redefinir la limitación de las personas con discapacidad visual. Con el cual se busca integrar la IA aplicado a Visión Artificial para actuar como un asistente personal que mediante palabras describa el entorno en el que se encuentra la persona.

El sistema de visión artificial cumple con la función de identificar y describir los objetos que rodean al usuario.

## Comenzando 

Descargar el codigo fuente de los repositorios de github

```
$  git clone https://github.com/akey96/VisionArtificial.git
```

Mira **Deployment** para conocer como desplegar el proyecto.en un ambiente de produccion


### Pre-requisitos 📋

Tener instalado:
- Python 3.6
- pip3
- virtualenv
- Sistema operativo Ubuntu 16.04
- Navegador Chrome


### Instalación 🔧

Ingresamos a la carpeta del proyecto
```
$  cd VisionArtificial/
```
Creamos el entorno virtual para las dependecias del proyecto con python y lo levantamos
```
$  virtualenv env --python=python3.6
$  source  env/bin/activate
```

Verificamos que la version de python se 3.6
```
$  python -V

Python 3.6.11
```

Verificamos la version de pip3 se la 20.1
```
$  pip3 -V

pip 20.1.1
```

Ingresamos al directorio en donde estan las dependencias
```
$  cd docker/
```
Instalamos las dependencias de python para el proyecto
```
$  pip3 install -r python_requirements.txt 
```
Instalamos algunas librerias necesarios en el sistema operativos para el procesamiento de imagenes con opencv
```
$  sudo apt install -y libsm6
$  sudo apt-get install libxrender1
```
Ingresamos al directorio en donde estan el codigo fuente del proyecto de la aplicacion
```
$  cd ../
$  cd scripts/
```
Levantamamos la aplicacion 

```
$  python app.py
```
Abrimos un navegador web visualizar la aplicacion en el puerto 5002
```
http://localhost:5002/
```

## Despliegue de la aplicacion en un ambiente de produccion

### Pre-requisitos
- Haber realizado los pasos anteriores

Tener instalado:
- Nginx (1.10.3 )
- Certbot

### Instalación 🔧
Agregamos repositorios de paquetes necesario para le sistema operativo
```
$  sudo add-apt-repository universe
$  sudo add-apt-repository ppa:certbot/certbot
```
Instalamos paquete necesarios en el sistema operativo
```
$  sudo apt-get install python-dev nginx software-properties-common certbot python3-certbot-nginx
```
Instalamos dependencias de la aplicacion para el despliegue
```
$  pip3 install  gunicorn  werkzeug==0.16.0
```
Ingresamos al directorio para probar la libreria
```
$ cd VisionArtificial/scripts/
```
Verificamos que el enlace al WSI del nginx este bien
```
$ gunicorn --bind 0.0.0.0:5002 wsgi:app
```
Agregar la configuracion del virtualhost del nginx que esta en el directorio configurations y el manejo de credenciales SSL para https
```
$ ls VisionArtificial/configurations
```
Reiniciamos el servidor nginx
```
$ sudo systemctl restart  nginx.service
```
## Autores

* **Alexander Mamani Yucra**  
* **Jose Enrique Camacho Silvestre.** 
* **Rudy Walter Martinez Melgarejo** 

