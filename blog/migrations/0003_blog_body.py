# Generated by Django 4.0.2 on 2022-03-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_blog_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="body",
            field=models.TextField(default=""),
        ),
    ]
