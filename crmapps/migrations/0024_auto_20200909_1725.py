# Generated by Django 3.1.1 on 2020-09-09 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapps', '0023_auto_20200830_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee_registration',
            old_name='DATE',
            new_name='date',
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
