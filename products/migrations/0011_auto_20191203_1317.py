# Generated by Django 2.2.8 on 2019-12-03 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20191203_1304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='products.Category', verbose_name='Родительские категория'),
        ),
    ]
