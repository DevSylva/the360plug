# Generated by Django 3.1.4 on 2020-12-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruise', '0008_auto_20201228_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(max_length=50, null=True)),
                ('cost', models.FloatField()),
            ],
        ),
    ]
