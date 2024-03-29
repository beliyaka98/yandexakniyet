# Generated by Django 4.0.4 on 2022-06-18 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_child_id_children_childid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='main',
            name='uid',
        ),
        migrations.AlterField(
            model_name='main',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='main',
            name='parentId',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='main',
            name='type',
            field=models.CharField(max_length=255),
        ),
    ]
