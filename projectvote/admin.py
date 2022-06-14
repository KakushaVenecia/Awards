from django.contrib import admin
from .models import Profile, Project, Comment,Rate, Rating

# Register your models here.
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Rate)
admin.site.register(Rating)
