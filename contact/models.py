'''Esses model s'ao a configuracao das tabelas da nossa base de dados'''

from ast import Try
from pyexpat import model
from django.db import models
from django.utils import timezone

# Create your models here.
# sempre que fizer qualquer alteração no models executar // python manage.py makemigrations
# para executar a migração e atualizar a base de dados // python manage.py migrate


class Category(models.Model):
    # classe que configura os meus dados na exibicao (Django model meta optios)
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


# tabela que de contatos
class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    # blank=True  informa que este campo é opicional
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    # campo descrição do cadastro
    description = models.TextField(blank=True)
    # exibe o registro
    show = models.BooleanField(default=True)
    # usuario pode inserir uma imagem
    picture = models.ImageField(blank=True, upload_to='picture/%Y/%m/')

    # configurando a tabela category como uma chave estrangeira na tabela contato
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
