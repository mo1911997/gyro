# Generated by Django 2.2.1 on 2019-06-27 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leave',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
