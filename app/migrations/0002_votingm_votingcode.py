# Generated by Django 3.2.9 on 2022-12-10 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votingm',
            name='votingcode',
            field=models.IntegerField(default=0),
        ),
    ]
