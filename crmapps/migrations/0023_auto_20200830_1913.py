# Generated by Django 3.0.8 on 2020-08-30 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapps', '0022_auto_20200827_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountnumber', models.CharField(max_length=100, null=True)),
                ('ifsccode', models.CharField(max_length=100, null=True)),
                ('bankname', models.CharField(max_length=100, null=True)),
                ('bankaddress', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ed_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification', models.CharField(max_length=100, null=True)),
                ('institute', models.CharField(max_length=100, null=True)),
                ('year', models.CharField(max_length=100, null=True)),
                ('percent', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee_registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FIRSTNAME', models.CharField(max_length=100, null=True)),
                ('LASTNAME', models.CharField(max_length=100, null=True)),
                ('DATE', models.CharField(max_length=100, null=True)),
                ('MONTH', models.CharField(max_length=100, null=True)),
                ('YEAR', models.CharField(max_length=100, null=True)),
                ('phonenumber', models.CharField(max_length=100, null=True)),
                ('emailid', models.CharField(max_length=100, null=True)),
                ('GENDER', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='employee_salary_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=100, null=True)),
                ('salary', models.CharField(max_length=100, null=True)),
                ('DATE', models.CharField(max_length=100, null=True)),
                ('MONTH', models.CharField(max_length=100, null=True)),
                ('YEAR', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ex_det',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100, null=True)),
                ('from_date', models.CharField(max_length=100, null=True)),
                ('to_date', models.CharField(max_length=100, null=True)),
                ('position', models.CharField(max_length=100, null=True)),
                ('reason', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='other_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FATHERNAME', models.CharField(max_length=100, null=True)),
                ('MOTHERNAME', models.CharField(max_length=100, null=True)),
                ('Address', models.CharField(max_length=100, null=True)),
                ('City', models.CharField(max_length=100, null=True)),
                ('Zip', models.CharField(max_length=100, null=True)),
                ('Aadharnumber', models.CharField(max_length=100, null=True)),
                ('Driverlicense', models.CharField(max_length=100, null=True)),
                ('emergencycontactno2', models.CharField(max_length=100, null=True)),
                ('emergencycontactno1', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='user_man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
                ('role', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='tab',
        ),
        migrations.DeleteModel(
            name='tab2',
        ),
    ]