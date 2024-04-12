# Generated by Django 5.0.4 on 2024-04-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sneacers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('cost', models.IntegerField(verbose_name='cost')),
                ('description', models.TextField(default='no description', max_length=500, verbose_name='description')),
                ('img', models.ImageField(upload_to='images/', verbose_name='img')),
            ],
        ),
    ]