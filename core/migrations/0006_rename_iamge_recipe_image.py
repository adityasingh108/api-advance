# Generated by Django 3.2.8 on 2021-10-23 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_recipe_iamge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='iamge',
            new_name='image',
        ),
    ]
