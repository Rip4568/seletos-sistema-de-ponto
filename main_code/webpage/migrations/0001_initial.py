# Generated by Django 4.1.1 on 2022-10-18 09:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employeeInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=12)),
                ('sobrenome', models.CharField(max_length=15)),
                ('admissão', models.DateField()),
                ('idade', models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(10)])),
                ('sexo', models.CharField(max_length=8)),
                ('aniversário', models.DateField()),
                ('endereço', models.CharField(max_length=50)),
                ('CPF', models.IntegerField(validators=[django.core.validators.MaxValueValidator(11), django.core.validators.MinValueValidator(11)])),
            ],
        ),
    ]