# Generated by Django 2.1.7 on 2019-03-13 16:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paidordersnc1',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='paidordersnc2',
            name='item_id',
        ),
        migrations.RemoveField(
            model_name='paidordersnc3',
            name='item_id',
        ),
    ]
