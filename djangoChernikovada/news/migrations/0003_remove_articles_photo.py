# Generated by Django 5.0.6 on 2024-06-12 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_articles_options_articles_author_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='photo',
        ),
    ]
