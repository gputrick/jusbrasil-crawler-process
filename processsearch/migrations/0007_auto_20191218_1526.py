# Generated by Django 3.0 on 2019-12-18 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processsearch', '0006_process_process_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='process_number',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
