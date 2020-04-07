# django-docs

# Python Web Development Workflow

1- **conda create -n ENV_NAME python=x.x django=x.x**
a- create install the right versions of django and python

b- **conda activate ENV_NAME**

c- **conda deactivate** when finished

2- create a new django project **django-admin startproject _name of project_**

3- start a server **python3 manage.py runserver**

4- create an app in the project **python3 manage.py startapp _name of app_**

---

---

## NEXT

-   create a view (a function that takes a request and responds with some output)

-   url renderer (use the include function from django.conf.urls)

-   regular expression for url matches (url(r'^\$', views.index, name="index"))

-   settings.py

-- add resources:

--- BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(**file**)))

--- TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")

--- STATIC_DIR = os.path.join(BASE_DIR, "static")

-- add apps created to INSTALLED_APPS list.

-- notify the static folder for loading static resources: STATIC_URL = '/static/'
STATICFILES_DIRS = [
STATIC_DIR,
]

### html injection (TEMPLATES)

-   for static to be loaded add:
    <!DOCTYPE html>

    {% load staticfiles %}

-   for dynamic loading: {{ insert_me }}

-   for static: \<img src="{% static "PATH" %}" alt="gcp services" />

### Models

-   create the models in
    class Topic(models.Model):
    top_name = models.CharField(max_length=264, unique=True)

        def **str**(self):
        return self.top_name

-   call **python manage.py migrate**
-   call **python manage.py makemigrations _APP_NAME_**
-   again call **python manage.py migrate**
-   tell admin.py about the models
