# Generated by Django 4.1.5 on 2023-01-09 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menuobject_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuobject',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
