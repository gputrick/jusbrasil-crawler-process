# Generated by Django 3.0 on 2019-12-20 00:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Process',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('process_number', models.CharField(max_length=255, unique=True)),
                ('kind', models.TextField()),
                ('area', models.TextField()),
                ('subject', models.TextField()),
                ('distribuition', models.TextField()),
                ('judge', models.TextField()),
                ('action_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='RelatedPart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processsearch.Process')),
            ],
        ),
        migrations.CreateModel(
            name='RelatedPeople',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('related_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processsearch.RelatedPart')),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('description', models.TextField()),
                ('process', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='processsearch.Process')),
            ],
        ),
    ]