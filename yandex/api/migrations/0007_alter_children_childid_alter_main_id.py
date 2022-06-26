# Generated by Django 4.0.4 on 2022-06-18 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_rename_parentid_children_main'),
    ]

    operations = [
        migrations.AlterField(
            model_name='children',
            name='childId',
            field=models.UUIDField(unique=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False, unique=True),
        ),
    ]
