# Generated by Django 5.0.6 on 2024-09-21 21:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievement',
            name='news_name_for_achv',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='achievements', to='about.news'),
        ),
    ]
