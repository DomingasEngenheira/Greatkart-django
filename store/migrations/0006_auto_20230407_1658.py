# Generated by Django 3.1 on 2023-04-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_merge_20230407_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='variation',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
