# Generated by Django 4.0.4 on 2022-06-07 18:13

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_customuser_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': (('view_pizza', 'Can view pizza'),)},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='test',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_blog',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_team',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default=datetime.datetime(2022, 6, 7, 18, 13, 18, 140365, tzinfo=utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone',
            field=models.CharField(max_length=100, null=True),
        ),
    ]