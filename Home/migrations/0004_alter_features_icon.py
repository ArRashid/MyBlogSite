# Generated by Django 4.0.4 on 2022-06-04 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_features_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/icons/features'),
        ),
    ]
