from django.db import models
from products.models import make_thumbnail
from django.utils.timezone import now


class Idea(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Заголовок")
    text = models.TextField(max_length=512, verbose_name=u"Текст")
    image = models.ImageField(upload_to='static/img/products/', verbose_name=u"Изображение", blank=True)
    image_thumb = models.ImageField(upload_to='static/img/products/', blank=True, editable=False)
    is_main = models.BooleanField(default=False, verbose_name=u"На главной")
    is_active = models.BooleanField(default=True, verbose_name=u"Актуален")
    date = models.DateTimeField(editable=False, default=now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Идея"
        verbose_name_plural = u"Идеи"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.image_thumb):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super(Idea, self).save(*args, **kwargs)
