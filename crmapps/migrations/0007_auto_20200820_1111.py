# Generated by Django 3.0.8 on 2020-08-20 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapps', '0006_other_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee_registration',
            name='DATE',
        ),
        migrations.RemoveField(
            model_name='employee_registration',
            name='MONTH',
        ),
        migrations.RemoveField(
            model_name='employee_registration',
            name='YEAR',
        ),
    ]