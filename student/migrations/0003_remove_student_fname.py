# Generated by Django 2.1.1 on 2018-11-20 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20181116_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='fname',
        ),
    ]
