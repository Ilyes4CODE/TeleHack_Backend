# Generated by Django 5.0.2 on 2024-02-29 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0008_remove_tickettech_client_tickettech_center_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickettech',
            name='address',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
