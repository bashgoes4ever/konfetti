from django.db import models
from products.models import make_thumbnail


class Review(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Имя")
    text = models.TextField(max_length=512, verbose_name=u"Отзыв")
    image = models.ImageField(upload_to='static/img/reviews/', verbose_name=u"Изображение", blank=True)
    image_thumb = models.ImageField(upload_to='static/img/reviews/', blank=True, editable=False)
    is_active = models.BooleanField(default=True, verbose_name=u"Актуален")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Отзыв"
        verbose_name_plural = u"Отзывы"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.image_thumb):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super(Review, self).save(*args, **kwargs)
