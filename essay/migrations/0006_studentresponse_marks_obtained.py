# Generated by Django 3.2.7 on 2025-02-28 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('essay', '0005_alter_studentresponse_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresponse',
            name='marks_obtained',
            field=models.FloatField(default=0.0),
        ),
    ]
