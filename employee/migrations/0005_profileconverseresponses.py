# Generated by Django 2.2.1 on 2019-06-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_leaveconverseresponses'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileConverseResponses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=400)),
            ],
        ),
    ]