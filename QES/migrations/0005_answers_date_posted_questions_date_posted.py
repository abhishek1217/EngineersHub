# Generated by Django 4.0.4 on 2022-04-20 18:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('QES', '0004_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answers',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questions',
            name='date_posted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
