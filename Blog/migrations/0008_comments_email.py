# Generated by Django 4.0.4 on 2022-06-16 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='email',
            field=models.EmailField(default='no@email.exist', max_length=254),
        ),
    ]
