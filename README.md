# Little Lemon - Back-End Developer Capstone

Proyecto desarrollado como parte del curso **Meta Back-End Developer**.

Este proyecto implementa una aplicación web y una API REST para el restaurante **Little Lemon**, utilizando Django, Django REST Framework, Djoser y autenticación mediante tokens.

---

## Tecnologías utilizadas

- Python
- Django
- Django REST Framework
- Djoser
- MySQL
- Token Authentication
- HTML
- Git
- GitHub

---

## API Endpoints

### Página principal

```text
GET /
```

Muestra la página principal de la aplicación Little Lemon.

---

### Menu Items

Obtener todos los elementos del menú:

```text
GET /api/menu-items/
```

Crear un nuevo elemento del menú:

```text
POST /api/menu-items/
```

Ejemplo de respuesta:

```json
[
  {
    "id": 1,
    "title": "Greek Salad",
    "price": "8.50",
    "inventory": 20
  },
  {
    "id": 2,
    "title": "Star Wars",
    "price": "2.45",
    "inventory": 14
  }
]
```

---

### Bookings

Obtener todas las reservas:

```text
GET /api/bookings/
```

Crear una nueva reserva:

```text
POST /api/bookings/
```

Los endpoints de reservas permiten gestionar la información relacionada con las reservas del restaurante.

---

## Autenticación de usuarios

El proyecto utiliza **Djoser** junto con **Token Authentication** para el registro e inicio de sesión de los usuarios.

### Registrar usuario

```text
POST /auth/users/
```

Ejemplo:

```json
{
  "username": "usuario1",
  "password": "Password123!",
  "email": "usuario@example.com"
}
```

---

### Obtener token de autenticación

```text
POST /auth/token/login/
```

Ejemplo:

```json
{
  "username": "usuario1",
  "password": "Password123!"
}
```

Respuesta esperada:

```json
{
  "auth_token": "TOKEN_GENERADO"
}
```

---

### Cerrar sesión

```text
POST /auth/token/logout/
```

Este endpoint requiere autenticación.

---

## Uso del Token

Para acceder a los endpoints protegidos se debe enviar el token mediante el encabezado HTTP:

```text
Authorization: Token <auth_token>
```

Ejemplo:

```text
Authorization: Token 1234567890abcdef
```

En Postman se puede agregar dentro de la sección **Headers**:

```text
Key: Authorization
Value: Token <auth_token>
```

---

## Panel de administración

Django incluye un panel de administración para gestionar los datos de la aplicación.

Ruta:

```text
/admin/
```

URL local:

```text
http://127.0.0.1:8000/admin/
```

Desde el panel de administración se pueden gestionar:

- Usuarios
- Tokens
- Grupos
- Menu Items
- Bookings

---

## Crear un superusuario

Para crear un administrador ejecutar:

```bash
python manage.py createsuperuser
```

Luego completar los datos solicitados:

```text
Username
Email
Password
```

Posteriormente se puede iniciar sesión en:

```text
http://127.0.0.1:8000/admin/
```

---

## Modelos principales

### MenuItem

Representa los elementos disponibles en el menú del restaurante.

Campos principales:

```text
title
price
inventory
```

Ejemplo:

```text
Greek Salad
Price: 8.50
Inventory: 20
```

---

### Booking

Representa las reservas realizadas por los clientes.

Puede almacenar información como:

```text
first_name
reservation_date
reservation_slot
```

Además, el sistema puede impedir reservas duplicadas dependiendo de la fecha y horario configurados.

---

## Base de datos

El proyecto utiliza **MySQL** como sistema de gestión de base de datos.

La configuración de conexión se encuentra en:

```text
littlelemon/settings.py
```

Ejemplo:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

Por seguridad, no se deben publicar contraseñas reales en GitHub.

---

## Crear la base de datos

Ejemplo utilizando MySQL:

```sql
CREATE DATABASE littlelemon
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
```

Luego se debe configurar correctamente la conexión dentro de `settings.py`.

---

## Migraciones

Para crear y aplicar las migraciones ejecutar:

```bash
python manage.py makemigrations
python manage.py migrate
```

Esto crea las tablas correspondientes en la base de datos.

---

## Instalación del proyecto

Clonar el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

Entrar a la carpeta del proyecto:

```bash
cd littlelemon
```

Activar el entorno virtual:

```bash
pipenv shell
```

Instalar las dependencias:

```bash
pipenv install
```

---

## Dependencias principales

El proyecto utiliza dependencias como:

```text
Django
djangorestframework
djoser
mysqlclient
```

Estas dependencias se encuentran administradas mediante:

```text
Pipfile
Pipfile.lock
```

---

## Ejecutar el proyecto

Para iniciar el servidor de desarrollo:

```bash
python manage.py runserver
```

La aplicación estará disponible en:

```text
http://127.0.0.1:8000/
```

---

## Rutas principales

```text
http://127.0.0.1:8000/
```

Página principal.

```text
http://127.0.0.1:8000/admin/
```

Panel de administración.

```text
http://127.0.0.1:8000/api/menu-items/
```

API de elementos del menú.

```text
http://127.0.0.1:8000/api/bookings/
```

API de reservas.

```text
http://127.0.0.1:8000/auth/users/
```

Registro y gestión de usuarios.

```text
http://127.0.0.1:8000/auth/token/login/
```

Obtención del token de autenticación.

```text
http://127.0.0.1:8000/auth/token/logout/
```

Cierre de sesión.

---

## Probar la API

La API puede probarse utilizando:

- Navegador de Django REST Framework
- Postman
- Insomnia

Ejemplo:

```text
GET http://127.0.0.1:8000/api/menu-items/
```

Con autenticación:

```text
Authorization: Token <auth_token>
```

---

## Ejemplo con Postman

### Obtener elementos del menú

Método:

```text
GET
```

URL:

```text
http://127.0.0.1:8000/api/menu-items/
```

Header:

```text
Authorization: Token <auth_token>
```

Respuesta esperada:

```text
200 OK
```

---

## Pruebas unitarias

El proyecto contiene pruebas unitarias para comprobar el funcionamiento de los componentes principales.

Ejecutar:

```bash
python manage.py test
```

Resultado esperado:

```text
OK
```

También se puede comprobar la configuración general de Django con:

```bash
python manage.py check
```

Resultado esperado:

```text
System check identified no issues.
```

---

## Estructura del proyecto

```text
littlelemon/
│
├── littlelemon/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── restaurant/
│   ├── migrations/
│   ├── templates/
│   │   └── index.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── manage.py
├── Pipfile
├── Pipfile.lock
└── README.md
```

---

## Funcionalidades implementadas

- Aplicación web desarrollada con Django
- API REST desarrollada con Django REST Framework
- Base de datos MySQL
- Gestión de elementos del menú
- Gestión de reservas
- Registro de usuarios
- Inicio de sesión
- Cierre de sesión
- Autenticación mediante Token
- Integración con Djoser
- Panel de administración de Django
- Gestión de usuarios desde el panel de administración
- Gestión de tokens
- Serialización de datos
- Endpoints protegidos
- Pruebas unitarias
- Integración con Postman o Insomnia
- Proyecto preparado para GitHub

---

## Seguridad

Las credenciales reales no deben almacenarse directamente en repositorios públicos.

Evitar publicar:

```text
Contraseña de MySQL
Contraseña del superusuario
Tokens de autenticación
SECRET_KEY de producción
```

Los valores mostrados en este README son únicamente ejemplos.

---

## Git y GitHub

Inicializar Git:

```bash
git init
```

Agregar archivos:

```bash
git add .
```

Crear commit:

```bash
git commit -m "Complete Little Lemon Back-End Capstone"
```

Agregar repositorio remoto:

```bash
git remote add origin <URL_DEL_REPOSITORIO>
```

Subir el proyecto:

```bash
git push -u origin main
```

---

## Autor

**Alcindo Chavarria**

Proyecto realizado para:

**Meta Back-End Developer Professional Certificate**

Coursera / Meta