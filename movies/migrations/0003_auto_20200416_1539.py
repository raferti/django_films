# Generated by Django 3.0.5 on 2020-04-16 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200416_1323'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Review',
            new_name='Reviews',
        ),
    ]
