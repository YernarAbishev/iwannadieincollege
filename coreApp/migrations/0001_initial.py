# Generated by Django 3.1 on 2023-02-10 03:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('company', models.CharField(max_length=255, verbose_name='Компания')),
                ('postDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('logo', models.CharField(max_length=500, verbose_name='Логотип (Ссылка на изображение)')),
                ('description', models.TextField(verbose_name='Описание')),
                ('isActive', models.BooleanField(default=True, verbose_name='Добавить/Убрать')),
                ('linkJob', models.CharField(max_length=500, verbose_name='Ссылка на вакансию')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
            },
        ),
        migrations.CreateModel(
            name='Practice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('company', models.CharField(max_length=255, verbose_name='Компания')),
                ('postDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата публикации')),
                ('logo', models.CharField(max_length=500, verbose_name='Логотип (Ссылка на изображение)')),
                ('description', models.TextField(verbose_name='Описание')),
                ('isActive', models.BooleanField(default=True, verbose_name='Добавить/Убрать')),
                ('linkCompany', models.CharField(max_length=500, verbose_name='Ссылка на компашку')),
            ],
            options={
                'verbose_name': 'Практика',
                'verbose_name_plural': 'Практики',
            },
        ),
    ]
