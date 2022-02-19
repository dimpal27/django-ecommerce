# Generated by Django 4.0.2 on 2022-02-04 10:58

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BillingAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Street_Address', models.CharField(max_length=100)),
                ('Apartment_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Countries', models.CharField(max_length=50)),
                ('Zip', models.CharField(max_length=100)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(max_length=10)),
                ('E_mail', models.EmailField(max_length=254)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.user')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('quantity', models.IntegerField(default=1)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.product')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.user')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Street_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Apartment_Address', models.CharField(blank=True, max_length=100, null=True)),
                ('Countries', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('Zip', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('E_mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.user')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField()),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('ordered_date', models.DateTimeField()),
                ('ordered', models.BooleanField(default=False)),
                ('billing_Address', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.billingadress')),
                ('item', models.ManyToManyField(to='client.CartItem')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.user')),
            ],
        ),
    ]
