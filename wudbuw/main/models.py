from django.db import models


class Sneacers(models.Model):
    name = models.CharField('name', max_length=100)
    cost = models.IntegerField('cost')
    description = models.TextField('description', max_length=500, default='no description')
    img = models.ImageField(("img"), upload_to='images/', height_field=None, width_field=None, max_length=None)
    def __str__(self):
        return self.name

class User(models.Model):
    mail = models.CharField('mail', max_length=100, unique=True)
    password = models.CharField('password', max_length=100)
    def __str__(self):
        return self.mail
