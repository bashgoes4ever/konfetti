from django.db import models
from classess import SingletonModel


class Contacts(SingletonModel.SingletonModel):
    city = models.CharField(max_length=128, blank=True, null=True, default=u"Владивосток", verbose_name=u"Город")
    street = models.CharField(max_length=128, blank=True, null=True, default=u"ул. Адмирала Юмашева 35", verbose_name=u"Улица, дом")
    email = models.CharField(max_length=128, blank=True, null=True, default=u"konfetti@mail.ru", verbose_name=u"Email")
    phone1 = models.CharField(max_length=128, blank=True, null=True, default=u"89510183672", verbose_name=u"Телефон 1")
    phone2 = models.CharField(max_length=128, blank=True, null=True, default=u"89146773888", verbose_name=u"Телефон 2")
    working_hours = models.CharField(max_length=128, blank=True, null=True, default=u"пн-пт 9-17, сб-вс: 9-14", verbose_name=u"Часы работы")
    map = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Код яндекс карты")
    whatsapp = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"WhatsApp")
    viber = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"Viber")
    telegram = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"Telegram")
    vk = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"Vkontakte")
    instagram = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"Instagram")
    facebook = models.CharField(max_length=128, blank=True, null=True, verbose_name=u"Facebook")
    price_list = models.FileField(upload_to='static/pricelist/', verbose_name=u"Прайс", blank=True)

    def __str__(self):
        return u"Контакты"

    class Meta:
        verbose_name = u"Контакты"
        verbose_name_plural = u"Контакты"
