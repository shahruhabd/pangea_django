# Generated by Django 3.2.13 on 2023-05-13 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='archived',
            field=models.BooleanField(default=False),
        ),
    ]
