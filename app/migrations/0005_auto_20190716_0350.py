# Generated by Django 2.2.3 on 2019-07-16 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_empresa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servico',
            old_name='servico',
            new_name='trabalhos',
        ),
    ]