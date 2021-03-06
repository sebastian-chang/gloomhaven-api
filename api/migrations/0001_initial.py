# Generated by Django 3.2 on 2021-05-03 05:00

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('class_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('initials', models.CharField(max_length=5)),
                ('starting', models.BooleanField(default=False)),
                ('symbol', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=100)),
                ('color', models.CharField(max_length=20)),
                ('xp_per_level', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('hp_per_level', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
                ('story', models.TextField(blank=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Perk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('perk_id', models.CharField(max_length=20)),
                ('quantity', models.IntegerField()),
                ('action', models.CharField(max_length=100)),
                ('character_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='perks', to='api.characterclass')),
            ],
        ),
    ]
