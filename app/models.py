from django.db import models
from django.conf import settings

# Create your models here.

zonas = [
    ('Z1','Zona Norte'),
    ('Z2','Zona Sul'),
    ('Z3', 'Zona Leste'),
    ('Z4','Zona Oeste'),
    ('Z5','Centro')
]

regiao = [
    ('AR', 'Água Rasa'),
    ('AG', 'Anhanguera'),
    ('AC', 'Aricanduva'),
    ('AA', 'Artur Alvim'),
    ('BF', 'Barra Funda'),
    ('BV', 'Bela Vista'),
    ('BL', 'Belém'),
    ('BR', 'Brás'),
    ('BT', 'Butantã'), 
    ('CC', 'Cachoeirinha'),
    ('CA', 'Cambuci'),
    ('CB', 'Campo Belo'),
    ('CL', 'Campo Limpo'),
    ('CG', 'Cangaíba'),
    ('CR', 'Capão Redond'),
    ('CO', 'Carrão'),
    ('CV', 'Casa Verde'),
    ('CM', 'Cidade Ademar'),
    ('CD', 'Cidade Dutra'),
    ('CL', 'Cidade Líder'), 
    ('CT', 'Cidade Tiradentes'),
    ('CS', 'Consolação'),
    ('DI', 'Diadema'), 
    ('EM', 'Ermelino Matarazzo'),
    ('FO', 'Freguesia do Ó'),
    ('GU', 'Guarujá'),
    ('GN', 'Guianazes'),
    ('IG', 'Iguatemi'),
    ('IP', 'Ipiranga'),
    ('IB', 'Itaim Bibi'), 
    ('IT', 'Itaquera'),
    ('JB', 'Jabaquara'), 
    ('JE',  'Jaguaré'),
    ('JG', 'Jardim Ângela'),
    ('JP', 'Jardim Paulista'),
    ('JS', 'Jardim São Luís'),
    ('LP', 'Lapa'),
    ('LB', 'Liberdade'), 
    ('LM', 'Limão'),
    ('MO', 'Moema'),
    ('MC', 'Mooca'),
    ('MB', 'Morumbi'),
    ('PD', 'Pedreira'),
    ('PN', 'Penha' ),
    ('PI', 'Pinheiros'),
    ('PB', 'Pirituba'),
    ('RT', 'Raposo Tavares'),
    ('RP',  'República'),
    ('RQ', 'Rio Pequeno'), 
    ('SM', 'Sacomã'),
    ('SC', 'Santa Cecília'),
    ('SN', 'Santana'),
    ('SA', 'Santo Amaro'),
    ('SD', 'São Domingos'), 
    ('SU', 'Saúde'),
    ('SE', 'Sé'),
    ('SO', 'Socorro'),
    ('TB', 'Tremembé'),
    ('TC', 'TucuruvI'),
    ('VA', 'Vila Andrade'),
    ('VC', 'Vila Curuçá'),
    ('VF' ,'Vila Formosa'),
    ('VG', 'Vila Guilhermina'),
    ('VL', 'Vila Leopoldina'),
    ('VM', 'Vila Matilde'),
    ('VP', 'Vila Prudente'),
    ('VS', 'Vila Sônia'),
]


especialidade= [
    ('A', 'Acupuntura'),
    ('AL', 'Alergia e Imunologia'),
    ('AN', 'Anestesiologia'), 
    ('AG', 'Angiologia'),
    ('CC', 'Cancerologia'), 
    ('CD', 'Cardiologia'),
    ('CM', 'Clínica Médica'), 
    ('DM', 'Dermatologia'),
    ('EN', 'Endocrinologia'), 
    ('ED', 'Endoscopia'),
    ('GR', 'Geriatria'), 
    ('GN', 'Ginecologia'),
    ('HM', 'Hematologia'), 
    ('HO', 'Homeopatia'),
    ('IF', 'Infectologia'),
    ('NU', 'Neurologia'),
    ('OB', 'Obstetrícia'),
    ('OF', 'Oftalmologia'), 
    ('OT', 'Ortopedia'), 
    ('OR', 'Otorrinolaringologia'),
    ('PT', 'Patologia'), 
    ('PD', 'Pediatria'),
    ('PM', 'Pneumologia'),
    ('PS', 'Psiquiatria'),
    ('RD', 'Radiologia'),
    ('RT', 'Radioterapia'),
    ('RM', 'Reumatologia'),
    ('UR', 'Urologia'),
]

def buscar_sigla_especialidade(busca):
    for item in especialidade:
        if busca.lower() == item[1].lower():
            return item[0]
    return None

class Cadastro(models.Model):
    nome = models.CharField(max_length=50, default="")
    nascimento = models.DateTimeField(blank=True, null=True)
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