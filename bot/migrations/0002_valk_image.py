# Generated by Django 5.0.3 on 2024-03-31 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='valk',
            name='image',
            field=models.CharField(default=None, max_length=255, null=True),
        ),
    ]
