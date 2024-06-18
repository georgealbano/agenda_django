from pyexpat import model
from django.db import models
from django.utils import timezone
# Create your models here.
# sempre que fizer qualquer alteração no models executar // python manage.py makemigrations
# para executar a migração e atualizar a base de dados // python manage.py migrate


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # blank=True  informa que este campo é opicional
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    descripition = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
