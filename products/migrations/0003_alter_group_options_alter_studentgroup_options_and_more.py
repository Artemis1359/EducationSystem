# Generated by Django 4.2.10 on 2024-03-01 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'ordering': ('name',), 'verbose_name': 'Группа', 'verbose_name_plural': 'Группы'},
        ),
        migrations.AlterModelOptions(
            name='studentgroup',
            options={'ordering': ('id',), 'verbose_name': 'Студент в группе', 'verbose_name_plural': 'Студенты в группах'},
        ),
        migrations.AlterModelOptions(
            name='userproduct',
            options={'ordering': ('id',), 'verbose_name': 'Товар клиента', 'verbose_name_plural': 'Товары клиентов'},
        ),
        migrations.AddConstraint(
            model_name='studentgroup',
            constraint=models.UniqueConstraint(fields=('student', 'group'), name='unique_student_group'),
        ),
        migrations.AddConstraint(
            model_name='userproduct',
            constraint=models.UniqueConstraint(fields=('client', 'product'), name='unique_client_product'),
        ),
    ]
