# Generated by Django 4.1.1 on 2024-11-05 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0008_alter_categoriamanutencao_titulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='horario',
            field=models.TimeField(blank=True, null=True),
        ),
    ]