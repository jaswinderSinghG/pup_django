# Generated by Django 2.1.3 on 2018-12-01 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20181201_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentbox',
            name='Date_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
