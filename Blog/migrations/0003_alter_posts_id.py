# Generated by Django 4.0.4 on 2022-06-10 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_posts_tages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]