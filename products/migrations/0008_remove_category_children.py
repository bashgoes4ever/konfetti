# Generated by Django 2.2.8 on 2019-12-03 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_category_children'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='children',
        ),
    ]
