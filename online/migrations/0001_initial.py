# Generated by Django 4.2.8 on 2024-02-01 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, unique=True)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('phone', models.IntegerField(max_length=10)),
            ],
        ),
    ]
