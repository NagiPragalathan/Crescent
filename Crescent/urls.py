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
    path('birac_edit',views.birac_edit),
    path('birac_save',views.birac_save),
    path('delete_birac',views.delete_birac),
    path('set_birac',views.set_birac),



    path('logo',views.update_logo),
    path('upload_logo',views.upload_logo),
    path('delete_logo',views.delete_logo),
    path('set_logo',views.set_logo),

    path('carrer',views.carrer),
    path('update_carrer',views.update_carrer),
    path('edit_eventform',views.edit_eventform),


    path('eventform',views.eventform),
    path('update_eventform',views.update_eventform),
    path('delete_form',views.delete_form),
    path('convert_excel',views.convert_excel),
    
    
    path('list_blog',views.list_blog),
    path('list_edit_blog',views.list_edit_blog),
    path('view_blog/<str:pk>',views.view_blog),
    path('edit_blog/<str:pk>',views.edit_blog),
    path('blog_edit',views.blog_edit),
    path('save_blog',views.save_blog),
    path('delete_blog',views.delete_blog),
    path('edit_blog/save_edit_blog/<int:pk>',views.save_edit_blog),

    path('testimonicals',views.Testimonicals),
    path('testimonicals_edit',views.Testimonicals_edit),
    path('testimonicals_save',views.Testimonicals_save),

    path('events',views.events),
    path('events_save',views.events_save),
    path('events_edit',views.events_edit),

    path('tbi',views.tbi),
    path('tbi_edit',views.tbi_edit),
    path('tbi_save',views.tbi_save),
    path('delete_tbi',views.delete_tbi),
    path('set_tbi',views.set_tbi),

    path('sisfs',views.sisfs),
    path('sisfs_edit',views.sisfs_edit),
    path('sisfs_save',views.sisfs_save),
    path('delete_sisfs',views.delete_sisfs),
    path('set_sisfs',views.set_sisfs),

path("about",views.about),
path("angelInvestor",views.angelInvestor),
path("globalMarket",views.GlobalMarket),
path("EDI",views.EDI),
path("Home",views.home),
path("Mentor_Connect",views.MentorConnect),
path("Mentor_Clinic",views.MentorClinic),

path("new_ventures",views.newVentures),
path("ourstartups",views.ourStartups),
path("samridth",views.samridth),
path("service",views.service),
path("sisfs",views.sisfs),
path("stategovtfunds",views.stategovtfunds),
path("testimonial",views.testimonial),
path("MBA",views.Mba),
path ("birac",views.birac),
path("career",views.career),
path("gallery",views.gallery),
path("demo",views.demo),

path("about",views.about),
path("startupTN",views.startupTN),
path("events",views.eventsTBI),

path("home_edit",views.home_edit),


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

