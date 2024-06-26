# Generated by Django 5.0.1 on 2024-03-23 19:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_query"),
    ]

    operations = [
        migrations.CreateModel(
            name="Faq",
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
                ("question", models.TextField(blank=True, null=True)),
                ("answer", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "FAQ",
                "managed": False,
            },
        ),
    ]
