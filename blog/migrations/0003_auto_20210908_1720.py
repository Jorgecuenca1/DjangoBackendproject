# Generated by Django 3.2.7 on 2021-09-08 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210908_1702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='adress',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='excerpt',
            new_name='nit',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='slug',
            new_name='phone',
        ),
    ]
