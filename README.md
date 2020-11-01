<img alt="Logo" src="https://i.imgur.com/vt6aCKB.png" width="100" height="100">

# Proyecto-Integrador-Django [![GitHub release](https://img.shields.io/badge/release-none-blue)](https://github.com/MaximoSav/Proyecto-Integrador-Django/releases) [![Language](https://img.shields.io/badge/lang-espa%C3%B1ol%20%2F%20english-yellow)](#)
Proyecto realizado por Franco Benito y Maximo Savino del Instituto Técnico Salesiano Villada (ITSV).
 
<img alt="GitHub issues" src="https://img.shields.io/github/issues/MaximoSav/Proyecto-Integrador-Django?style=for-the-badge&logo=appveyor">
<img alt="GitHub forks" src="https://img.shields.io/github/forks/MaximoSav/Proyecto-Integrador-Django?style=for-the-badge&logo=appveyor">

## Diagramas:
 - Diagrama de Clases: https://lucid.app/invitations/accept/eae58af3-3696-43c9-adb1-4cd1f43eea5a
 - Diagrama de Casos de Uso: https://lucid.app/invitations/accept/e59f30f5-17fb-4cfc-b96d-572ae9c4a63d
## Aplicaciones necesarias
### Python
 - Versión: 3
 - Documentación: https://docs.python.org/es/3/

## Uso
### Requisitos
| Paquete | Version |
|:---|:---:|
| Django| 2.2 |
| django-jet| 1.0.8 |
| google-api-python-client| 1.4.1 |
| httplib2| 0.18.1 |
| oauth2client| 4.1.3 |
| Pillow| 7.2.0 |
| pkg-resources| 0.0.0 |
| pyasn1| 0.4.8 |
| pyasn1-modules| 0.2.8 |
| pytz| 2020.1 |
| rsa| 4.6 |
| six| 1.15.0 |
| sqlparse| 0.4.1 |
| uritemplate| 3.0.1 |

### Instruccciones
#### Instalacion manual

```shell
git clone https://github.com/MaximoSav/Proyecto-Integrador-Django.git ~/.ProyectoDjango
cd ~/.ProyectoDjango
pip install -r requirements.txt
python core/manage.py makemigrations
python core/manage.py migrate
python core/manage.py collectstatic
```

#### Creacion de superusuario

```shell
cd ~/.ProyectoDjango
python core/manage.py createsuperuser
```

#### Ejecución post-instalación

Para correr la aplicación debe ingresar esto en la terminal:

```shell
cd ~/.ProyectoDjango
python core/manage.py runserver
```
