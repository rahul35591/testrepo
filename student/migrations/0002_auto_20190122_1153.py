# Generated by Django 2.1.5 on 2019-01-22 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='sid',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]