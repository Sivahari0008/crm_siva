# Generated by Django 3.0.8 on 2020-08-21 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crmapps', '0012_employee_salary_details_other_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='other_details',
            new_name='other_detail',
        ),
    ]
