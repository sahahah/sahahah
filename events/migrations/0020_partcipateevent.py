# Generated by Django 5.0.1 on 2024-03-11 18:55

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_remove_feedback_timestamp_alter_feedback_comment_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='partcipateEvent',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('phone', models.CharField(db_column='phone', max_length=200, null=True)),
                ('email', models.CharField(db_column='email', max_length=200, null=True)),
                ('part_event_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_size', models.ForeignKey(db_column='team_size', null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.events')),
                ('user', models.ForeignKey(db_column='user', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
