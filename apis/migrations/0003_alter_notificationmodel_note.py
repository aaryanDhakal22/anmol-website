# Generated by Django 4.0.2 on 2022-07-17 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_rename_formonth_notificationmodel_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notificationmodel',
            name='note',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]
