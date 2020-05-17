# Generated by Django 3.0.6 on 2020-05-17 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0010_remove_customerdebitcredit_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ordered_set', to='accounts_app.Customer'),
        ),
    ]
