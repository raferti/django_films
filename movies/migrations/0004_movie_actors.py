# Generated by Django 3.0.5 on 2020-04-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_auto_20200416_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='film_actor', to='movies.Actor', verbose_name='актеры'),
        ),
    ]
