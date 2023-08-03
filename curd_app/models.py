from django.db import models

class Project(models.Model):

    pro_lang = [("JAVA","JAVA"),("PYTHON","PYTHON"),("c++","c++"),("REACT","REACT")]

    project_name = models.CharField(max_length=50)
    project_description = models.TextField()
    project_lead = models.CharField(max_length=40)
    programming_language = models.CharField(max_length=200, choices=pro_lang)
    project_start_date = models.DateField()
    project_delivery_date = models.DateField()