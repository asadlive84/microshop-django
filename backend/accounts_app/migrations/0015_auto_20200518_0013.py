# Generated by Django 3.0.6 on 2020-05-17 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0014_auto_20200518_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerdebitcredit',
            name='customer_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customerdebitcredit_set', to='accounts_app.Account'),
        ),
    ]
