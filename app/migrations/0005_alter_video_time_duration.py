# Generated by Django 5.0.6 on 2024-07-09 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_lesson_video"),
    ]

    operations = [
        migrations.AlterField(
            model_name="video",
            name="time_duration",
            field=models.IntegerField(null=True),
        ),
    ]
