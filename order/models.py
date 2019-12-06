from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Имя", blank=True)
    phone = models.CharField(max_length=128, verbose_name=u"Телефон", blank=False)
    text = models.TextField(max_length=500, verbose_name=u"Комментарий", blank=True)
    t = models.CharField(max_length=128, verbose_name=u"Тип", blank=False)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.t

    class Meta:
        verbose_name = u"Заявка"
        verbose_name_plural = u"Заявки"

