# Generated by Django 5.0.1 on 2024-03-11 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0018_feedback'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feedback',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(),
        ),
    ]
