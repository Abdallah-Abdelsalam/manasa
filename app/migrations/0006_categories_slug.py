# Generated by Django 5.0.6 on 2024-07-13 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_alter_video_time_duration"),
    ]

    operations = [
        migrations.AddField(
            model_name="categories",
            name="slug",
            field=models.SlugField(max_length=255, null=True),
        ),
    ]