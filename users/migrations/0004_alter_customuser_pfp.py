# Generated by Django 4.0.4 on 2022-06-07 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_pfp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='pfp',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/users/profiles', verbose_name='Profile Pic'),
        ),
    ]