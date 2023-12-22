# Proyecto-Django-Lista-Tareas

Creación de un entorno virtual
1 Abre el CMD y  entra en la carpeta en donde quieres crear el entorno virtual.
2 Ejecuta python -m venv mi_entorno.
3  Activa el entorno virtual con mi_entorno\Scripts\activate.

Instalación
Instala el framework Django y Django REST Framework con los siguientes comandos:
pip install django
pip install djangorestframework

Creación de proyecto
Crea el proyecto con el nombre tarea_project con el comando django-admin startproject tarea_project.
Accede a la carpeta del proyecto con cd tarea_project.
Crea una aplicación dentro del proyecto con python manage.py startapp tarea_app.

Configuración 
Abre el archivo tarea_project/settings.py.
Agrega el nombre de tu aplicación a la lista INSTALLED_APPS.

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/3e189cbe-347e-42a2-aa1f-74822ee1f3f1)

Definición  del modelo

En el archivo tarea_app/models.py

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/cc002fd4-a298-45a1-8649-9a7664f36105)

Realizamos las migraciones con los siguientes comando en consola
Crea  las migraciones para el  modelo de estudiante para definir cómo se estructurará la base de datos
python manage.py makemigrations myapp


 Luego, aplicamos las migraciones para crear la tabla en la base de datos
python manage.py migrate

Serializando

Creamos el archivo tarea_app/serializers.py:

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/97c70274-ddf5-45df-ad00-4ee81c41d8ff)

Vista basada en clase para la API
En el archivo tarea_app/views.py:

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/da296dfc-dbf0-4cb5-b853-587edc0687a8)

Configuración de las URL
Creamos el archivo urls.py dentro de tarea_app, configura las URL para la vista:

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/8e4394c1-8709-4925-89b6-e840cda3df05)

y luego en el archivo urls.py del proyecto:

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/45ebb0f7-d7d9-488c-ad10-dcac9ab475b4)

Probamos el proyecto
 con el siguiente comando   python manage.py runserver

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/2c2796e6-2517-4ded-a42e-2ca7b1beabd4)

De este modo podremos obtener una url para acceder a todas la vistas del  proyecto, para esto  debemos escojer la que necesitamos esto nos dirigira  al endpoint que definimos anteriormente.

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/3fcc9619-71fd-4921-9e5d-a17381b948c8)

Django Templates
Crearemos la carpeta templates dentro de tarea_app, luego  tarea_app/templates en donde crearemos nuestros templates con html
tarea_app/templates/base.html

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/c9cf4e07-6722-42fa-912e-932abbfaa3b8)

Configuramos los campos necesarios y personalizamos las etiquetas para la vizualizacion en el template.

tarea_app/templates/tareas_detalle.html

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/afbebf41-a6af-407c-b81f-eeb1d1c9e605)

tarea_app/templates/tareas_detalle.html

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/7b610e58-f23a-4997-8e6e-28621a53777d)

tarea_app/templates/tarea_completada.html

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/d83c989d-1a18-40eb-baa6-7b76552af951)

Ya listos los  templates en html tengan la informacion y rutas correspondientes, podemos  agregarle estilos a nuestra vista.

Para los estilos creamos la carpeta static dentro de blog tarea_app/static/tarea_app/style.css

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/bf6bc584-e37d-4d78-819a-6cc3e7e464e9)

Usando el endpoint "/admin/", podras acceder al administrador de usuarios y modelos de django restframework.

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/9241568e-1a1a-4f03-a2bc-0dce6bbeb84b)

Veremos  una vista previa de lo que seria la vista de las tareas:

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/bccb4afd-98aa-45f2-af03-ce9e656603f9)

Aqui podras ver el endpoint que nos muestra las tareas que tenemos completadas:

![image](https://github.com/Tatianabarbosa16/Proyecto-Django-Lista-Tareas/assets/139836257/677717eb-f502-4e10-b053-9a5356b54166)






















