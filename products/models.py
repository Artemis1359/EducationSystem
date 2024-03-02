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
    min_group_size = models.SmallIntegerField(default=1)
    max_group_size = models.IntegerField(default=1000)

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

    class Meta:
        ordering = ('name',)
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return f'{self.name}'


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

    class Meta:
        ordering = ('id',)
        verbose_name = 'Студент в группе'
        verbose_name_plural = 'Студенты в группах'
        constraints = [
            models.UniqueConstraint(
                fields=('student', 'group'),
                name='unique_student_group'
            )
        ]

    def __str__(self):
        return f'{self.student}  {self.group}'


class UserProduct(models.Model):
    """ Вспомогательный класс для пользователей приобретающих товар"""

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

    class Meta:
        ordering = ('id',)
        verbose_name = 'Товар клиента'
        verbose_name_plural = 'Товары клиентов'
        constraints = [
            models.UniqueConstraint(
                fields=('client', 'product'),
                name='unique_client_product'
            )
        ]

    def __str__(self):
        return f'{self.product}  {self.client}'