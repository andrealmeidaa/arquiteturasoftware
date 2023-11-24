from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Raca(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
class Gato(models.Model):
    sexo_opts= [
        ('M', 'Macho'),
        ('F', 'Fêmea'),
    ]
    nome = models.CharField(max_length=50)
    raca = models.ForeignKey(Raca, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=1,choices=sexo_opts)
    data_cadastro = models.DateTimeField(default=timezone.now)
    data_nascimento=models.DateField()
    adotado=models.BooleanField(default=False)
    descricao=models.TextField()

    def __str__(self):
        return self.nome
    
    def calcular_idade(self):
        dias= timezone.now().date() - self.data_nascimento

        if dias.days > 365:
            return f'{dias.days//365} anos'
        elif dias.days > 30:
            return f'{dias.days//30} meses'
        elif dias.days > 7:
            return f'{dias.days} dias'

class Usuario(models.Model):
    estados_br = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espirito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]
    nome = models.CharField(max_length=50)
    user=models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    data_cadastro = models.DateTimeField(default=timezone.now)
    cpf=models.CharField(max_length=11,primary_key=True)
    endereco=models.CharField(max_length=100)
    def __str__(self):
        return self.nome
 
    def save(self, *args, **kwargs):
        if self.pk is None:  # se é uma nova instância
            user = User.objects.create_user(username=self.nome, email=self.email)
            self.user = user
        super().save(*args, **kwargs)

class Adocao(models.Model):
    status_opts=[
        ('1','Em análise'),
        ('2','Reprovada'),
        ('3','Aprovada')
    ]
    gato=models.ForeignKey(Gato,on_delete=models.CASCADE)
    adotante=models.ForeignKey(Usuario,on_delete=models.CASCADE)
    data_criacao=models.DateTimeField(default=timezone.now)
    data_analise=models.DateTimeField(null=True,blank=True)
    data_aprovacao=models.DateTimeField(null=True,blank=True)
    status=models.CharField(max_length=1,choices=status_opts,default='1')
    
    def __str__(self):
        return f'{self.gato} - {self.status}'