# Generated by Django 5.0.2 on 2024-02-29 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0004_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Base.client'),
        ),
    ]
