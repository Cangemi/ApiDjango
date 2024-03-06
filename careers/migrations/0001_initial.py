# Generated by Django 5.0.3 on 2024-03-06 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("username", models.CharField(max_length=100)),
                ("created_datetime", models.DateTimeField(auto_now_add=True)),
                ("title", models.CharField(max_length=255)),
                ("content", models.TextField()),
            ],
        ),
    ]
