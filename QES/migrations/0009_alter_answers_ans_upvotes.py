# Generated by Django 4.0.4 on 2022-04-23 12:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QES', '0008_remove_answers_downvotes_remove_answers_upvotes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='ans_upvotes',
            field=models.ManyToManyField(related_name='a_upvotes', to=settings.AUTH_USER_MODEL),
        ),
    ]
