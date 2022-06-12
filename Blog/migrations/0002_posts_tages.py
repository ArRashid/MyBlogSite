# Generated by Django 4.0.4 on 2022-06-10 18:11

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='tages',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
