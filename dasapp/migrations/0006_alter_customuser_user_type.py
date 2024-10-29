# Generated by Django 5.0.6 on 2024-10-27 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dasapp', '0005_alter_customuser_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[(2, 'doc'), (1, 'admin')], default=1, max_length=50),
        ),
    ]