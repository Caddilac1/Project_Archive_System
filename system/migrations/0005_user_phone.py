# Generated by Django 5.1.6 on 2025-02-12 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0004_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
