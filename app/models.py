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
      
class loja(models.Model):

    produtos_opcoes =[
       ('Mercado', 'Mercado'),
       ('Livros','Livros'),
       ('Roupas','Roupas'),
       ('Eco-vegan','Eco-vegan'),
       ('On-line','On-line'),
       ('Cosmeticos','Cosmeticos'),
    ]

    nome = models.CharField(max_length=30)
    descricao = models.TextField(default='')
    lugar = models.CharField(max_length=50)
    produtos = models.CharField(max_length=20, choices=produtos_opcoes)
    foto = models.ImageField(upload_to='media')

    def __str__(self):
       return self.nome

class restaurante(models.Model):

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

    nome = models.CharField(max_length=90)
    descricao = models.TextField(max_length=200, default='')
    qualidade = models.PositiveIntegerField()
    categoria = models.CharField(max_length=20, choices=tipo_opcoes)
    nivel_avaliacao = models.PositiveIntegerField(choices=nivel_avaliacao)
    foto = models.ImageField(upload_to='', default='')

class servico(models.Model):

    servico_opcoes = [
       ('delivery', 'Delivery'),
       ('nutricionista', 'Nutricionista'),
       ('dicas', 'Dicas'),
       ('auxilio', 'Auxilio'),
    ]

    nome = models.CharField(max_length=100)
    descricao = models.TextField( max_length=300)
    foto = models.ImageField(upload_to='', default='')
    trabalhos = models.CharField(max_length=20, choices=servico_opcoes, default='')

    def __str__(self):
        return self.nome

class Contato(models.Model):
    nome = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=40, default='')
    telefone = models.CharField(max_length=15, default='')
    assunto = models.CharField(max_length=50, default='')
    mensagem = models.TextField(max_length=100, default='')

    def __str__(self):
        return self.assunto

class empresa(models.Model):

    endereco = models.CharField(max_length=60, default='')
    foto = models.ImageField(upload_to='', default='')
    empresa = models.CharField(max_length=50, default='')
    email = models.EmailField(null=False)

    def __str__(self):
        return self.empresa

    
