# Generated by Django 5.0.6 on 2024-10-28 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0007_alter_customuser_user_type_billing'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Billing',
        ),
    ]
