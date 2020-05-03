# Generated by Django 2.1.3 on 2018-12-01 08:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181127_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentbox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Comment', models.TextField(max_length=1000)),
                ('Date_time', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
