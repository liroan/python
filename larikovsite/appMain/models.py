from django.db import models

# Create your models here.

class MainPageM(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст", default=None)
