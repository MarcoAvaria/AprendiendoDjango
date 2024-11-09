"""
URL configuration for AprendiendoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import miapp.views
#import view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', miapp.views.index, name="index"),
    path('inicio/', miapp.views.index, name="inicio"),
    path('hola-mundo/', miapp.views.hola_mundo, name="hola-mundo"),
    path('pagina-pruebas/', miapp.views.pagina, name="pagina-pruebas"),
    path('pagina-pruebas/<int:redirigir>', miapp.views.pagina, name="pagina-pruebas"),
    path('contacto/', miapp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/', miapp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellidos>', miapp.views.contacto, name="contacto"),
    path('crear-articulo/<str:title>/<str:content>/<str:public>', miapp.views.crear_articulo, name="crear_articulo"),
    path('articulo/', miapp.views.articulo, name="articulo"),
    path('editar-articulo/<int:id>', miapp.views.editar_articulo),
    path('articulos/', miapp.views.articulos, name='articulos'),
    path('borrar-articulo/<int:id>', miapp.views.borrar_articulo, name="borrar"),
    path('save-article', miapp.views.save_article, name="save"),
    path('create-article', miapp.views.create_article, name="create"),
]
