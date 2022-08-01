"""FinalVCQ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from finalapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cursos/', views.cursos, name = "cursos"),
    path('carreras/', views.carreras, name = "carreras"),
    path('save-curso/', views.save_curso, name = "save_curso"),
    path('crear-curso/',views.crear_curso,name="crear_curso"),
    path('crear-carrera/',views.crear_carrera,name="crear_carrera"),
    path('eliminar-curso/<int:id>',views.eliminar_curso,name='eliminar_curso')


]
