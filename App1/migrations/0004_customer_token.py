# Generated by Django 4.1.7 on 2023-04-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0003_delete_passwordreset'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='token',
            field=models.TextField(blank=True, null=True),
        ),
    ]
