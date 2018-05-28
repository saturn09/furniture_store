from django.db import models


# Create your models here.


class Cloth(models.Model):
    name = models.CharField(max_length=60, verbose_name='Наименование предмета')
    description = models.TextField(max_length=200, verbose_name='Описание предмета')
    reduced_from = models.DecimalField(verbose_name='Старая цена за предмет', decimal_places=2, max_digits=10)
    price = models.DecimalField(verbose_name='Цена за предмет', decimal_places=2, max_digits=10)
    img = models.ImageField(verbose_name='Картинка', upload_to='clothes', null=True)
