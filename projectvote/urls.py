from django.urls import re_path as url, path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.main, name='index'),
    url(r'^userlogin$', views.userlogin, name='userlogin'),
    url(r'^register$', views.register, name='register'),
    url(r'^signout$',views.signout, name='signout'),
    url(r'^post$', views.post, name='post'),
    path('projects', views.projects, name='projects'),
    url(r'^project-details/(\d+)/$', views.project_details, name='project-details'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'^update$', views.update_profile, name='update'),
    url(r'^search$', views.search_project, name='search'),
    path('api/profiles/', views.ProfileList.as_view(), name='api_profiles'),
    path('api/projects/', views.ProjectList.as_view(), name='api_projects'), 
   

    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)