# Generated by Django 3.2.9 on 2022-02-15 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='devicestatus',
            name='switch',
            field=models.IntegerField(choices=[(0, 0), (1, 1)], default=0),
        ),
    ]