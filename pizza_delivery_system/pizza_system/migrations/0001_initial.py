# Generated by Django 3.0.7 on 2020-06-05 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TodoModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo_description', models.CharField(max_length=300)),
                ('todo_created_date', models.DateField()),
                ('todo_modified_date', models.DateField()),
            ],
        ),
    ]
