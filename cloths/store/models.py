from django.contrib.auth.models import User
from django.db import models


class ClothsDataManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=True)


class ClothsData(models.Model):
    title = models.CharField(max_length=55, verbose_name='Название')
    color = models.CharField(max_length=45, verbose_name='Цвет')
    price = models.IntegerField(verbose_name='Цена')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    cat = models.ForeignKey('CategoryData', on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, related_name='user_name')
    like = models.ManyToManyField(User, verbose_name='Лайки', blank=True, related_name='like_name')

    objects = models.Manager()
    tmp = ClothsDataManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вещь'
        verbose_name_plural = 'Вещи'


class Like(models.Model):
    LIKE_CHOICES = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(ClothsData, on_delete=models.CASCADE, related_name='post_name')
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)


class CategoryData(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'




    




