# Generated by Django 4.1.5 on 2023-01-09 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_menuobject_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuobject',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='menu.menuobject'),
        ),
    ]
