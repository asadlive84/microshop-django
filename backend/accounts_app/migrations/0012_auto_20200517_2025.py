# Generated by Django 3.0.6 on 2020-05-17 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts_app', '0011_auto_20200517_2002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'ordering': ['-created_at']},
        ),
    ]
