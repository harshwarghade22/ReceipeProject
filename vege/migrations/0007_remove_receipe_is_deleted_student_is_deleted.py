# Generated by Django 5.0.2 on 2024-02-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_receipe_is_deleted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='student',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]
