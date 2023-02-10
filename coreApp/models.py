from django.db import models
from datetime import datetime

class Job(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    company = models.CharField("Компания", max_length=255)
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    logo = models.CharField("Логотип (Ссылка на изображение)", max_length=500)
    description = models.TextField("Описание")
    isActive = models.BooleanField("Добавить/Убрать", default=True)
    linkJob = models.CharField("Ссылка на вакансию", max_length=500)

    def __str__(self):
        return f"{self.title} - {self.company} - {self.postDate}"

    class Meta:
        verbose_name = "Вакансия"
        verbose_name_plural = "Вакансии"


class Practice(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    company = models.CharField("Компания", max_length=255)
    postDate = models.DateTimeField("Дата публикации", default=datetime.now)
    logo = models.CharField("Логотип (Ссылка на изображение)", max_length=500)
    description = models.TextField("Описание")
    isActive = models.BooleanField("Добавить/Убрать", default=True)
    linkCompany = models.CharField("Ссылка на компашку", max_length=500)

    def __str__(self):
        return f"{self.title} - {self.company} - {self.postDate}"

    class Meta:
        verbose_name = "Практика"
        verbose_name_plural = "Практики"