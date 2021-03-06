# Generated by Django 2.1 on 2021-05-01 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method_name', models.CharField(max_length=120)),
                ('img', models.FileField(upload_to='')),
                ('slug', models.SlugField(default='slug_here', max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
