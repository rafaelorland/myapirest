# Generated by Django 4.2.4 on 2023-08-13 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projetos', '0002_projetos_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='projetos',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
