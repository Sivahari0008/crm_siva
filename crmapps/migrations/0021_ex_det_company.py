# Generated by Django 3.0.8 on 2020-08-26 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapps', '0020_auto_20200826_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='ex_det',
            name='company',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
