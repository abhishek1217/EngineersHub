# Generated by Django 4.0.4 on 2022-04-20 21:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QES', '0005_answers_date_posted_questions_date_posted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='upvotes',
        ),
        migrations.AddField(
            model_name='questions',
            name='upvotes',
            field=models.ManyToManyField(related_name='qes_questions', to=settings.AUTH_USER_MODEL),
        ),
    ]
