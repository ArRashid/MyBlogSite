# Generated by Django 4.0.4 on 2022-06-04 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('details', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='uploads/icons/features')),
            ],
        ),
    ]