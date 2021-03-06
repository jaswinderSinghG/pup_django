# Generated by Django 2.1.3 on 2020-04-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_auto_20200409_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Name_Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_admin_pic', models.FileField(upload_to='AdminPics/')),
                ('base_admin_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Home_Dynamic_Pics',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_dynamic_images', models.FileField(upload_to='dynamicPics_folder/')),
            ],
        ),
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
            name='home_dynamic_images',
        ),
        migrations.AlterField(
            model_name='home_page_pics_article',
            name='home_fixed_image',
            field=models.FileField(upload_to='homeImagesFixed'),
        ),
    ]
