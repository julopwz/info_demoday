# Generated by Django 2.2.3 on 2019-07-15 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20190715_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('endereco', models.CharField(default='', max_length=60)),
                ('foto', models.ImageField(default='', upload_to='')),
                ('empresa', models.CharField(default='', max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
