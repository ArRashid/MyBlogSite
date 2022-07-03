# Generated by Django 4.0.4 on 2022-07-03 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0008_rename_pid_review_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='analogy',
            old_name='pid',
            new_name='product',
        ),
        migrations.RenameField(
            model_name='link',
            old_name='review_id',
            new_name='review',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='pid',
            new_name='product',
        ),
        migrations.RemoveField(
            model_name='review',
            name='bqulity',
        ),
        migrations.RemoveField(
            model_name='review',
            name='vform',
        ),
    ]
