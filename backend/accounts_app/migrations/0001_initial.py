# Generated by Django 3.0.6 on 2020-05-08 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone_number', models.CharField(max_length=100, verbose_name='Mobile Number')),
                ('address', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.FloatField()),
                ('product_price', models.FloatField()),
                ('customer_paid', models.FloatField()),
                ('paid_status', models.BooleanField(blank=True)),
                ('unpaid_money', models.FloatField(blank=True)),
                ('order_custom_date', models.DateTimeField(blank=True, null=True)),
                ('extra_info', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts_app.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='accounts_app.Customer')),
                ('paid_money', models.FloatField(blank=True, null=True)),
                ('unpaid_money', models.FloatField(blank=True, null=True)),
                ('paid_status', models.BooleanField(default=False)),
                ('extra_info', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ordered_items', models.ManyToManyField(to='accounts_app.Ordered')),
            ],
        ),
    ]
