# Generated by Django 4.0.4 on 2022-04-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_mypost_categories_mypost_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mypost',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='mypost',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
