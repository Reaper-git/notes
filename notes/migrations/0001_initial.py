# Generated by Django 4.2 on 2023-04-27 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Notes",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_created=True, null=True)),
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
            ],
        ),
    ]
