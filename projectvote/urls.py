from django.urls import re_path as url
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.main, name='index'),
    url(r'^userlogin$', views.userlogin, name='userlogin'),
    url(r'^register$', views.register, name='register'),
    url(r'^post$', views.post, name='post'),
    url(r'^projects$', views.projects, name='projects'),
    url(r'^project-details/(\d+)/$', views.project_details, name='project-details'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'^update$', views.update_profile, name='update'),
    url(r'^search$', views.search_project, name='search'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view())
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)