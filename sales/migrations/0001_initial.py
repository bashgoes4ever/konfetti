# Generated by Django 2.2.8 on 2019-12-05 01:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=512, verbose_name='Текст')),
                ('trigger', models.CharField(blank=True, max_length=128, verbose_name='Размер скидки')),
                ('image', models.ImageField(blank=True, upload_to='static/img/products/', verbose_name='Изображение')),
                ('image_thumb', models.ImageField(blank=True, editable=False, upload_to='static/img/products/')),
                ('is_active', models.BooleanField(default=True, verbose_name='Актуален')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
    ]
