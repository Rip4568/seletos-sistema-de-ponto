from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import (CharField, DateField, IntegerField, Model, ForeignKey, TimeField, RESTRICT, CASCADE)
from datetime import datetime, time



NOW = datetime.now



class Genero(Model):
    Genero = CharField(max_length=35)
    def __str__(self):
        return self.Genero

class Cargo(Model):
    cargo = CharField(max_length=50)
    def __str__(self):
        return self.cargo

class Funcionario(Model):
    nome = CharField(max_length=32)
    sobrenome = CharField(max_length=32)
    admissão = DateField()
    cargo = ForeignKey(Cargo, on_delete=RESTRICT,default="Sem_cargo_denifido",blank=True,null=True)
    idade = IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(10)
        ]
     )
    genero = CharField(max_length=30,choices=[
        ('Masculino','Masculino'),
        ('Feminino','Feminino'),
        ('NA','Prefiro não opinar')])
    aniversário = DateField()
    endereço = CharField(max_length=75)
    CPF = IntegerField()

    def __str__(self):
        return (f"{self.nome} {self.sobrenome}")

class CheckIn(Model):
    funcionario = ForeignKey(Funcionario, on_delete=RESTRICT)
    dia = DateField(default=NOW)
    entrada_manha = TimeField(auto_now=False, auto_now_add=False, default=time(0,0), null=True,blank=True)
    saida_manha = TimeField(auto_now=False, auto_now_add=False, default=time(0,0), null=True,blank=True)
    entrada_tarde = TimeField(auto_now=False, auto_now_add=False, default=time(0,0), null=True,blank=True)
    saida_tarde = TimeField(auto_now=False, auto_now_add=False, default=time(0,0), null=True,blank=True)

    def __str__(self):
        return (f"{self.funcionario} - {self.dia}")
