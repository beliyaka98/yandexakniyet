# Generated by Django 4.0.4 on 2022-06-26 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_main_uid_alter_main_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='uid',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
