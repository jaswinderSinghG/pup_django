# Generated by Django 2.1.3 on 2020-04-07 07:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_home_page_pics_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home_page_pics_article',
            name='base_admin_name',
        ),
        migrations.RemoveField(
            model_name='home_page_pics_article',
            name='base_admin_pic',
        ),
        migrations.RemoveField(
            model_name='home_page_pics_article',
            name='best_article',
        ),
        migrations.RemoveField(
            model_name='home_page_pics_article',
            name='home_fixed_image',
        ),
    ]
