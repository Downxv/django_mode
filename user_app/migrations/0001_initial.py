# Generated by Django 4.2.5 on 2023-09-12 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Man',
            fields=[
                ('uid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=30, unique=True)),
                ('age', models.IntegerField(default=18)),
                ('sex', models.BooleanField(default=True)),
                ('info', models.TextField(blank=True, null=True)),
                ('salary', models.FloatField(default=12.0)),
                ('money', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('birthday', models.DateField(auto_now_add=True)),
                ('birthday2', models.DateTimeField(auto_now=True)),
                ('icon', models.FileField(null=True, upload_to='statics/')),
                ('img', models.ImageField(null=True, upload_to='statics/')),
                ('utype', models.IntegerField(choices=[(1, 'a'), (2, 'b')], default=1, verbose_name='用户类型')),
            ],
            options={
                'db_table': 'user_app_man',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('age', models.IntegerField(default=18)),
                ('sex', models.CharField(max_length=10)),
                ('is_deleted', models.BooleanField(default=False)),
                ('uuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.man')),
            ],
        ),
    ]
