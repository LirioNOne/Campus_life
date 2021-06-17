from django.db import models
from django.contrib.auth.models import User


class CustomUser(models.Model):
    login = models.TextField('логин')
    password = models.TextField('пароль')
    salt = models.TextField('соль')
    email = models.EmailField('email')
    full_name = models.TextField('полное имя')
    profile_icon = models.TextField('изображение профиля', blank=True)
    self_info = models.TextField('личная информация', blank=True)
    is_admin = models.BooleanField('админ?', default=False)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Event(models.Model):
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_id')
    title = models.TextField('название')
    description = models.TextField('краткое описание')
    event_img = models.ImageField('изображение для события', upload_to='C:/media/event_images', blank=True)
    event_datetime = models.DateTimeField('время события')
    going_to_event = models.ManyToManyField(User, default=None, blank=True, related_name='going_to_event')

    def __str__(self):
        return self.title

    def num_going(self):
        return self.going_to_event.count()

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


EVENT_CHOICES = (
    ('Иду', 'Иду'),
    ('Не иду', 'Не иду'),
)


class GoingToEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    value = models.CharField(choices=EVENT_CHOICES, default='Иду', max_length=10)

    def __str__(self):
        return str(self.event)

    class Meta:
        verbose_name = 'Идущий на событие'
        verbose_name_plural = 'Идущие на события'
