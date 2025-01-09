# Generated by Django 5.1 on 2024-11-15 21:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_records', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
