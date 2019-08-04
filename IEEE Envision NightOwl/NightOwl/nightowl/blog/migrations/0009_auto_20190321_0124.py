# Generated by Django 2.1.5 on 2019-03-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_auto_20190320_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='paidordersnc1',
            name='filters',
            field=models.CharField(choices=[('a', 'Pending'), ('b', 'Delivered'), ('c', 'Rejected')], default='Delivered', max_length=1),
        ),
        migrations.AddField(
            model_name='paidordersnc2',
            name='filters',
            field=models.CharField(choices=[('a', 'Pending'), ('b', 'Delivered'), ('c', 'Rejected')], default='Delivered', max_length=1),
        ),
        migrations.AddField(
            model_name='paidordersnc3',
            name='filters',
            field=models.CharField(choices=[('a', 'Pending'), ('b', 'Delivered'), ('c', 'Rejected')], default='Delivered', max_length=1),
        ),
    ]
