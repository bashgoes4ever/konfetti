# Generated by Django 2.2.8 on 2019-12-02 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('slug', models.CharField(max_length=128, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Раздел',
                'verbose_name_plural': 'Разделы',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Название')),
                ('level', models.IntegerField(blank=True, default=0, verbose_name='Уровень')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=512, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, upload_to='static/img/categories/', verbose_name='Изображение')),
                ('image_thumb', models.ImageField(blank=True, editable=False, upload_to='static/img/categories/')),
                ('is_main', models.BooleanField(default=True, verbose_name='На главной')),
                ('children', models.ManyToManyField(blank=True, default=None, null=True, related_name='_category_children_+', to='products.Category', verbose_name='Дочерние категории')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Category', verbose_name='Родительская категория')),
                ('section', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Section', verbose_name='Раздел')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
    ]
