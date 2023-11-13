# Generated by Django 4.2.7 on 2023-11-07 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ztest_ztest1', '0014_auto_20220212_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cisco_config_result',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cisco_output',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ciscoconfig',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ciscoconfig',
            name='timestamp',
            field=models.CharField(default=1699332092.341674, max_length=30),
        ),
        migrations.AlterField(
            model_name='device_creds',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='hostdetails',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ipaddress',
            name='timestamp',
            field=models.CharField(default=1699332092.338998, max_length=30),
        ),
        migrations.AlterField(
            model_name='ipaddressandhostname',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='ipwithdetail',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
