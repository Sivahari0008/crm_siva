# Generated by Django 3.0.8 on 2020-08-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapps', '0009_employee_salary_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee_registration',
            name='GENDER',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
