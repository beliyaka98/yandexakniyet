# Generated by Django 4.0.4 on 2022-06-18 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_children_childid_alter_children_main'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Children',
        ),
    ]