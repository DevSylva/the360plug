# Generated by Django 3.0.4 on 2020-09-28 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0002_auto_20200927_2335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
