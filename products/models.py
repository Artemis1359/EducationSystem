from django.db import models

from users.models import User


class Product(models.Model):
    """Класс для продуктов."""

    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='products'
    )
    name = models.CharField(max_length=200)
    date = models.DateTimeField()
    price = models.IntegerField()

    class Meta:
        ordering = ('id',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Автор: {self.author}'


class Lesson(models.Model):
    """Класс для уроков."""

    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        related_name='lessons',
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=200)
    link = models.URLField()

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return f'{self.name}'


class Group(models.Model):
    """Класс для групп."""

    name = models.CharField(max_length=200)
    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        related_name='groups',
        on_delete=models.CASCADE
    )

    students = models.ManyToManyField(User, through='StudentGroup')


class StudentGroup(models.Model):
    """Вспомогательный класс для студентов в группе."""

    student = models.ForeignKey(
        User,
        verbose_name='Ученик',
        related_name='student_groups',
        on_delete=models.CASCADE
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        related_name='student_groups',
        on_delete=models.CASCADE
    )


class UserProduct(models.Model):
    """ Вспомогательный класс для пользователей приобревших товар"""

    product = models.ForeignKey(
        Product,
        verbose_name='Продукт',
        related_name='user_products',
        on_delete=models.CASCADE
    )
    client = models.ForeignKey(
        User,
        verbose_name='Клиент',
        related_name='user_products',
        on_delete=models.CASCADE
    )