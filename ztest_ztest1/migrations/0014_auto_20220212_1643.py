# Generated by Django 3.1 on 2022-02-12 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ztest_ztest1', '0013_auto_20220212_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciscoconfig',
            name='timestamp',
            field=models.CharField(default=1644664407.5305378, max_length=30),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='timestamp',
            field=models.CharField(default=1644664407.529533, max_length=30),
        ),
    ]
