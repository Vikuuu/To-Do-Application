# Generated by Django 4.2.4 on 2024-04-25 11:24

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("to_do", "0002_remove_taskmodel_description_taskmodel_updated_at"),
    ]

    operations = [
        migrations.RenameField(
            model_name="taskmodel",
            old_name="name",
            new_name="title",
        ),
    ]
