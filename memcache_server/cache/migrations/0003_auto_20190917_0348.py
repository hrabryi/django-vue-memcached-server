# Generated by Django 2.2.5 on 2019-09-17 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache', '0002_auto_20190917_0330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cache',
            name='id',
        ),
        migrations.AlterField(
            model_name='cache',
            name='key',
            field=models.CharField(max_length=250, primary_key=True, serialize=False, unique=True),
        ),
    ]