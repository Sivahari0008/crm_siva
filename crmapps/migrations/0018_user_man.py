# Generated by Django 3.0.8 on 2020-08-24 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapps', '0017_bank_det'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_man',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
