# Generated by Django 5.0.4 on 2024-05-03 13:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.IntegerField()),
                ('rating', models.FloatField()),
                ('number_in_stock', models.IntegerField()),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='genre_name', to='movies.genre')),
            ],
        ),
    ]