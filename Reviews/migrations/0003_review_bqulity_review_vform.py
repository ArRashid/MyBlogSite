# Generated by Django 4.0.4 on 2022-06-28 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_link_review_remove_product_id_product_pid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='bqulity',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='vform',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
