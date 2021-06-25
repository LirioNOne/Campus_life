from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Customers(User):
    GENDER = (
        ('man', 'Man'),
        ('woman', 'Woman')
    )

    birthday = models.DateField(verbose_name='Day of birth', null=True)
    course = models.CharField(max_length=2, verbose_name='Course')
    inform = models.TextField(verbose_name='Personal information')
    avatar = models.ImageField(verbose_name='avatar', blank=True, null=True, upload_to='images/')
    gender = models.CharField(max_length=6, choices=GENDER, default='man')

    @staticmethod
    def age(birthday):
        import datetime
        return int((datetime.date.today() - birthday).days / 365.25)

    def values(self):
        return Customers.objects.filter(field=self).first()[0]

    val = property(values)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @staticmethod
    def get_by_username(username):
        pass

    def __str__(self):
        return self.username
