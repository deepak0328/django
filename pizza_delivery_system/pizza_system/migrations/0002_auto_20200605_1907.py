# Generated by Django 3.0.7 on 2020-06-05 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_system', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='todo_created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='todomodel',
            name='todo_modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]