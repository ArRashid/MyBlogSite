# Generated by Django 4.0.4 on 2022-06-07 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_test'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'permissions': (('test', 'Can view pizza'),)},
        ),
    ]