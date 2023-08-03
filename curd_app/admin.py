from django.contrib import admin
from .models import Project

class Project_Admin(admin.ModelAdmin):
    list_display = ['id', 'project_name','project_lead']


admin.site.register(Project,Project_Admin)
 