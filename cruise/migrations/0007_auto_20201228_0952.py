# Generated by Django 3.1.4 on 2020-12-28 08:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0006_auto_20201228_0937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='emailAddress',
        ),
        migrations.RemoveField(
            model_name='message',
            name='firstName',
        ),
        migrations.RemoveField(
            model_name='message',
            name='lastName',
        ),
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='phoneNumber',
        ),
        migrations.RemoveField(
            model_name='message',
            name='seen',
        ),
    ]
