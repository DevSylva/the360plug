# Generated by Django 3.1.4 on 2020-12-27 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0003_subscriber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Subscriber',
        ),
    ]
