from django.db import models
from django.contrib.auth.models import User


# class CustomUser(models.Model):
#     login = models.TextField('логин')
#     password = models.TextField('пароль')
#     salt = models.TextField('соль')
#     email = models.EmailField('email')
#     full_name = models.TextField('полное имя')
#     profile_icon = models.TextField('изображение профиля', blank=True)
#     self_info = models.TextField('личная информация', blank=True)
#     is_admin = models.BooleanField('админ?', default=False)
#
#     def __str__(self):
#         return self.login
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'

class CustomUser(User):
    GENDER = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина')
    )

    birthday = models.DateField(verbose_name='День рождения', null=True)
    course = models.CharField(max_length=1, verbose_name='Курс')
    inform = models.TextField(verbose_name='Информация о себе', blank=True)
    avatar = models.ImageField(verbose_name='фото', blank=True, null=True, upload_to='images/')
    # gender = models.CharField(max_length=7, verbose_name='Пол', choices=GENDER, default='Мужчина')

    @staticmethod
    def age(birthday):
        import datetime
        return int((datetime.date.today() - birthday).days / 365.25)

    def values(self):
        return CustomUser.objects.filter(field=self).first()[0]

    val = property(values)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    @staticmethod
    def get_by_username(username):
        pass

    def __str__(self):
        return self.username


class Event(models.Model):
    creator_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator_id')
    title = models.TextField('название')
    description = models.TextField('краткое описание')
    event_img = models.ImageField('изображение для события', upload_to='C:/media/event_images', blank=True)
    event_datetime = models.DateTimeField(auto_now_add=True)
    going_to_event = models.ManyToManyField(User, default=None, blank=True, related_name='going_to_event')
    event_comments = models.ManyToManyField(User, default=None, blank=True, related_name='event_comments')

    def __str__(self):
        return self.title

    def num_going(self):
        return self.going_to_event.count()

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


EVENT_CHOICES = (
    ('Пойти', 'Пойти'),
    ('Уже иду', 'Уже иду'),
)


class GoingToEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    value = models.CharField(choices=EVENT_CHOICES, default='Пойду', max_length=10)

    def __str__(self):
        return str(self.event)

    class Meta:
        verbose_name = 'Идущий на событие'
        verbose_name_plural = 'Идущие на события'


class Comments(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, blank=True, null=True, on_delete=models.CASCADE, related_name='comments_event')
    comment_text = models.TextField('Текст комментария')
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.event.title, self.user)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
