"""Crescent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from base import views
from django.urls import path
from Crescent import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('admin',views.admin),

    path('gallery',views.gallery),
    path('upload_image',views.upload_image),
    path('delete_image',views.delete_image),
    
    path('team',views.aboutus),
    path('admin_team',views.admin_team),
    path('update_team',views.update_team),
    path('delete_team',views.delete_team),

    path('birac',views.birac),

    path('logo',views.update_logo),
    path('upload_logo',views.upload_logo),
    path('delete_logo',views.delete_logo),
    path('set_logo',views.set_logo),

    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

