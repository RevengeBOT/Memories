# Generated by Django 4.0.4 on 2022-04-12 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_mypost_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='image',
            field=models.ImageField(upload_to='post/img/'),
        ),
    ]
