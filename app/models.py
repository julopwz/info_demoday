from django.db import models
from django.conf import settings

class Cadastro(models.Model):
    nome = models.CharField(max_length=50, default="")
    nascimento = models.DateField(null=False)
    telefone = models.CharField(max_length=15, default="")
    email = models.EmailField(max_length=50, default="")
    username = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=20, default="")

    def __str__(self):
        return  self.username


class Lugar(models.Model):
    nome = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField(default='')
      
class Loja(models.Model):

    produtos_opcoes =[
       ('Mc', 'Mercado'),
       ('Lr','Livros'),
       ('Rp','Roupas'),
       ('Ev','Eco-vegan'),
       ('Ol','On-line'),
       ('Cm','Cosmeticos'),
    ]

    nome = models.CharField(max_length=30)
    descricao = models.TextField(default='')
    lugar = models.CharField(max_length=50)
    produtos = models.CharField(max_length=2, choices=produtos_opcoes)
    foto = models.ImageField(upload_to='', default='')

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
    descricao = models.TextField(default='')
    qualidade = models.PositiveIntegerField()
    categoria = models.CharField(max_length=20, choices=tipo_opcoes)
    nivel_avaliacao = models.PositiveIntegerField(choices=nivel_avaliacao)
    foto = models.ImageField(upload_to='', default='')

class Servico(models.Model):

    servico_opcoes = [
       ('delivery', 'Delivery'),
       ('nutricionista', 'Nutricionista'),
       ('dicas', 'Dicas'),
       ('auxilio', 'Auxilio'),
    ]

    nome = models.CharField(max_length=30)
    descricao = models.TextField( max_length=50)
    foto = models.ImageField(upload_to='', default='')
    servico = models.CharField(max_length=2, choices=servico_opcoes, default='')

class Contato(models.Model):
    nome = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=40, default='')
    telefone = models.CharField(max_length=15, default='')
    assunto = models.CharField(max_length=50, default='')
    mensagem = models.TextField(max_length=100, default='')

    def __str__(self):
        return self.assunto
