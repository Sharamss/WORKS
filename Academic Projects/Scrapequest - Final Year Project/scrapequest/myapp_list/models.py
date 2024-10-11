from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    content = models.TextField()  # This will store all relevant project information
    user = models.ForeignKey(User, on_delete=models.CASCADE)  

    def __str__(self):
        return self.content  
    
    
# keywords

class Keyword(models.Model):
    Keyword = models.TextField()


class KeywordUploadProxy(Keyword):
    class Meta:
        proxy = True
        verbose_name = 'Keyword Upload'
        verbose_name_plural = 'Keyword Uploads'
