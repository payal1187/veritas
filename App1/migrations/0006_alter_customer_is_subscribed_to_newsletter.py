# Generated by Django 4.1.7 on 2023-04-10 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0005_customer_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='is_subscribed_to_newsletter',
            field=models.BooleanField(default=True),
        ),
    ]