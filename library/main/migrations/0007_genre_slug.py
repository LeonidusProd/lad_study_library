# Generated by Django 4.2 on 2023-12-12 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_user_reading'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]