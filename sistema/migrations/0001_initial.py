# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agencia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('telefono', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombreDeEmpresa', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=100)),
                ('cuit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OfertaDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('informacionNecesaria', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
                ('activas', models.BooleanField()),
                ('empresa', models.ForeignKey(to='sistema.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=200)),
                ('fechaNac', models.EmailField(max_length=200)),
                ('activo', models.BooleanField()),
                ('sexo', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroDeEmpleados',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaDeContratacion', models.DateTimeField()),
                ('fechaDeBaja', models.DateTimeField()),
                ('desocupado', models.ForeignKey(to='sistema.Persona')),
                ('empresa', models.ForeignKey(to='sistema.Empresa')),
            ],
        ),
        migrations.CreateModel(
            name='TipoDeTrabajo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tipoDeTrabajo', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='persona',
            name='tipoDeTrabajo',
            field=models.ForeignKey(to='sistema.TipoDeTrabajo'),
        ),
        migrations.AddField(
            model_name='ofertadetrabajo',
            name='tipoDeTrabajo',
            field=models.ForeignKey(to='sistema.TipoDeTrabajo'),
        ),
    ]
