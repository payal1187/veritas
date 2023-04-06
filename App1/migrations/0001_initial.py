# Generated by Django 4.1.7 on 2023-03-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_no', models.CharField(blank=True, max_length=100, null=True)),
                ('parent_id', models.IntegerField(blank=True, null=True)),
                ('customer_type', models.CharField(blank=True, max_length=20, null=True)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('client_vat', models.CharField(blank=True, max_length=20, null=True)),
                ('passport_no', models.CharField(blank=True, max_length=20, null=True)),
                ('iban_no', models.CharField(blank=True, max_length=50, null=True)),
                ('contact_1', models.CharField(blank=True, max_length=15, null=True)),
                ('contact_2', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('company_name', models.CharField(blank=True, max_length=160, null=True)),
                ('activity_area', models.CharField(blank=True, max_length=200, null=True)),
                ('company_vat', models.CharField(blank=True, max_length=20, null=True)),
                ('language', models.CharField(blank=True, max_length=20, null=True)),
                ('internal_observations', models.TextField(blank=True, null=True)),
                ('is_subscribed_to_newsletter', models.BooleanField(default=False)),
                ('is_subscribed_to_catalog', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_buyer', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_received_text', models.BooleanField(default=False)),
                ('is_email_verified', models.BooleanField(default=False)),
                ('password', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'db_table': 'customers',
            },
        ),
    ]
