# Generated by Django 5.0.1 on 2024-02-05 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0003_author_image_alter_author_phone_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(null=True, upload_to='authors'),
        ),
    ]
