# Generated by Django 3.1.6 on 2021-03-22 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogInApp', '0013_auto_20210322_1248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdata',
            name='electricity_gas',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='electricity_heating',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='electricity_provider',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='electricity_renewable',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='electricity_type',
        ),
        migrations.AddField(
            model_name='carbondata',
            name='electricity_gas',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='electricity_heating',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='electricity_provider',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='electricity_renewable',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='electricity_type',
            field=models.CharField(default='Null', max_length=100),
        ),
    ]
