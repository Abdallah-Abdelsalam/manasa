# Generated by Django 5.0.6 on 2024-07-17 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0009_number"),
    ]

    operations = [
        migrations.RenameField(
            model_name="number",
            old_name="phone",
            new_name="number",
        ),
    ]