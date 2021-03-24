# Generated by Django 3.1.6 on 2021-03-22 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LogInApp', '0015_auto_20210322_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_utilities_desktop',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_utilities_laptop',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_waste_battery',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_waste_bio',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_waste_glass',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_waste_hardware',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_waste_paper',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_waste_plastic',
        ),
        migrations.RemoveField(
            model_name='registrationdata',
            name='office_water',
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_utilities_desktop',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_utilities_laptop',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_waste_battery',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_waste_bio',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_waste_glass',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_waste_hardware',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_waste_paper',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_waste_plastic',
            field=models.CharField(default='Null', max_length=100),
        ),
        migrations.AddField(
            model_name='carbondata',
            name='office_water',
            field=models.CharField(default='Null', max_length=100),
        ),
    ]