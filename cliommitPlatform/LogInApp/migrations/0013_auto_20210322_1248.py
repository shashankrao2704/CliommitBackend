# Generated by Django 3.1.6 on 2021-03-22 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogInApp', '0012_auto_20210322_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdata',
            name='electricity_amount',
        ),
        migrations.AddField(
            model_name='carbondata',
            name='electricity_amount',
            field=models.CharField(default='Null', max_length=100),
        ),
    ]
