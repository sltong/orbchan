# Generated by Django 4.1 on 2022-08-03 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("orbs", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="thread",
            name="original_poster",
        ),
    ]
