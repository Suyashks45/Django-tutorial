"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from home.views import *
from recipe.views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('',home),
    path('recipes/', recipes , name = 'recipes'),
    path('delete_recipe/<id>/', delete_recipe, name = 'delete_recipe'), 
    path('update-recipe/<int:id>/', update_recipe, name='update_recipe'),
    path('login/', login_page, name='login_page'),
    path('logout/', logout_page , name='logout_page'),
    path('register/', register_page, name='register_page'),
    path('contact/',contact),
    path('about/',about),
    path('success_page/',success_page),
    path('admin/', admin.site.urls),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
