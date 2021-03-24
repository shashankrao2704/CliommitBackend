# Generated by Django 3.1.6 on 2021-03-21 10:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('LogInApp', '0009_registrationdata_test_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationdata',
            name='test_field',
        ),
        migrations.CreateModel(
            name='CarbonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_field', models.CharField(default='Null', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LogInApp.registrationdata')),
            ],
            options={
                'ordering': ['test_field'],
            },
        ),
    ]
