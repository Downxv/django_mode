# Generated by Django 4.2.5 on 2023-09-12 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.CharField(default='0', max_length=10),
        ),
    ]
