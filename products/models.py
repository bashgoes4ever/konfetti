from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
import os
from django.utils.timezone import now


class Section(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Название")
    slug = models.CharField(max_length=128, verbose_name=u"Ссылка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Раздел"
        verbose_name_plural = u"Разделы"


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Название")
    section = models.ForeignKey(Section, blank=True, null=True, default=None,
                                    on_delete=models.SET_DEFAULT, verbose_name=u"Раздел")
    parent = models.ForeignKey("self", blank=True, null=True, default=None, related_name='children',
                                    on_delete=models.SET_DEFAULT, verbose_name=u"Родительская категория")
    level = models.IntegerField(verbose_name=u"Уровень", blank=True, default=0)
    title = models.CharField(max_length=128, verbose_name=u"Заголовок", blank=True)
    description = models.TextField(max_length=512, verbose_name=u"Описание", blank=True)
    image = models.ImageField(upload_to='static/img/categories/', verbose_name=u"Изображение", blank=True)
    image_thumb = models.ImageField(upload_to='static/img/categories/', blank=True, editable=False)
    is_main = models.BooleanField(default=False, verbose_name=u"На главной")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Категория"
        verbose_name_plural = u"Категории"

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1
        if not make_thumbnail(self.image, self.image_thumb):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super(Category, self).save(*args, **kwargs)


class Product(models.Model):
    name = models.CharField(max_length=128, verbose_name=u"Название")
    category = models.ManyToManyField(Category, blank=True, default=None, verbose_name=u"Родительские категория")
    price = models.IntegerField(verbose_name=u"Цена", default=0)
    image = models.ImageField(upload_to='static/img/products/', verbose_name=u"Изображение", blank=True)
    image_thumb = models.ImageField(upload_to='static/img/products/', blank=True, editable=False)
    is_main = models.BooleanField(default=False, verbose_name=u"На главной")
    is_active = models.BooleanField(default=True, verbose_name=u"Актуален")
    is_top = models.BooleanField(default=True, verbose_name=u"Популярный товар")
    date = models.DateTimeField(editable=False, default=now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Товар"
        verbose_name_plural = u"Товары"

    def save(self, *args, **kwargs):
        if not make_thumbnail(self.image, self.image_thumb):
            raise Exception('Could not create thumbnail - is the file type valid?')
        super(Product, self).save(*args, **kwargs)



def make_thumbnail(img, thumb):
    if img:
        """
        Create and save the thumbnail for the photo (simple resize with PIL).
        """
        max_width = 370
        max_height = 225

        image = Image.open(img)
        w, h = image.size
        if w > h:
            width = round(max_height/(h/w))
            thumb_size = (width, max_height)
        else:
            height = round(max_width/(w/h))
            thumb_size = (max_width, height)
        image.thumbnail(thumb_size, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(img.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False    # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        thumb.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

    return True
