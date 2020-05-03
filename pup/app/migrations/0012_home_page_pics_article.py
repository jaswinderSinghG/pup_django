# Generated by Django 2.1.3 on 2020-04-06 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20200405_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home_Page_Pics_Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('best_article', models.TextField(max_length=500)),
                ('base_admin_pic', models.FileField(upload_to='')),
                ('base_admin_name', models.CharField(max_length=100)),
                ('home_fixed_image', models.FileField(upload_to='')),
                ('home_dynamic_images', models.FileField(upload_to='')),
            ],
        ),
    ]
