# Generated by Django 5.0.1 on 2024-02-07 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('online', '0006_alter_author_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='c_name',
            new_name='name',
        ),
    ]
