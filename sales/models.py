from django.db import models
from products.models import make_thumbnail
from django.utils.timezone import now


class Sale(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Заголовок")
    text = models.TextField(max_length=512, verbose_name=u"Текст")
    trigger = models.CharField(max_length=128, verbose_name=u"Размер скидки", blank=True)
    image = models.ImageField(upload_to='static/img/products/', verbose_name=u"Изображение", blank=True)
    image_thumb = models.ImageField(upload_to='static/img/products/', blank=True, editable=False)
    is_active = models.BooleanField(default=True, verbose_name=u"Актуален")
    date = models.DateTimeField(editable=False, default=now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Акция"
        verbose_name_plural = u"Акции"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.image_thumb):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super(Sale, self).save(*args, **kwargs)
