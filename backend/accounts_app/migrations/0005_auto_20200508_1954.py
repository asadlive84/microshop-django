# Generated by Django 3.0.6 on 2020-05-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0004_auto_20200508_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='ordered_items',
            field=models.ManyToManyField(blank=True, null=True, to='accounts_app.Ordered'),
        ),
    ]