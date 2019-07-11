from django.conf import settings
from django.db import models
from django.utils import timezone


class Lugar(models.Model):
    nome = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo
        
class Loja(models.Model):

    produtos_opcoes =[
        ('Mc', 'Mercado'),
        ('Lr','Livros'),
        ('Rp','Roupas'),
        ('Ev','Eco-vegan'),
        ('Ol','On-line'),
        ('Cm','Cosmeticos'),
    ]

    preco = models.DecimalField(decimal_places=2, max_digits=10, default=30)
    lugar = models.CharField(max_length=30)
    nome = models.ForeignKey(Lugar, on_delete=models.SET_DEFAULT, default='')
    produtos = models.CharField(max_length=2, choices=produtos_opcoes)
    foto = models.ImageField(upload_to='', default = '')

    def __str__(self):
        return self.nome

class Restaurante(models.Model):

    tipo_opcoes = [
        ('vegano', 'Vegano'),
        ('vegetariano', 'Vegetariano'),
    ]

    nivel_avaliacao = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]

    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    qualidade = models.PositiveIntegerField()
    categoria = models.CharField(max_length=20, choices=tipo_opcoes)
    nivel_avaliacao = models.PositiveIntegerField(choices=nivel_avaliacao)
    foto = models.ImageField(upload_to='', default = '')

class Servico(models.Model):

    nome = models.CharField(max_length=30)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='', default = '')

