# Generated by Django 2.0.6 on 2018-11-13 21:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('estado', models.CharField(help_text='Informe apenas a sigla', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo', max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animais.Cidade')),
            ],
        ),
    ]
