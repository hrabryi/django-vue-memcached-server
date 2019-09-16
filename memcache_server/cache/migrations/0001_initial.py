# Generated by Django 2.2.5 on 2019-09-16 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cache',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=250, unique=True)),
                ('value', models.CharField(blank=True, max_length=250)),
                ('exptime', models.BigIntegerField(verbose_name='Expiration time')),
                ('bytes_length', models.BigIntegerField(db_column='bytes', verbose_name='number of bytes')),
            ],
        ),
    ]
