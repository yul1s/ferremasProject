# Generated by Django 5.2.1 on 2025-05-22 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_remove_cliente_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='rut',
            field=models.CharField(blank=True, max_length=12, null=True, unique=True),
        ),
    ]
