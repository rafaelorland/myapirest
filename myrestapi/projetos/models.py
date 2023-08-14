from django.db import models
from users.models import Profile
import uuid

class Projetos(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField(null = True, blank = True)
    created = models.DateTimeField(auto_created = True)
    img = models.ImageField(upload_to='images/', null = True, blank = True) 
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    owner = models.ForeignKey(Profile , on_delete = models.SET_NULL, blank = True, null = True)
   
    
    def __str__(self):
        return (f'Titulo:  {self.title}')