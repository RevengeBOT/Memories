# Generated by Django 4.0.4 on 2022-04-12 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_alter_mycategory_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycategory',
            name='image',
            field=models.ImageField(upload_to='category/static/category/img/'),
        ),
    ]