# Generated by Django 2.2.7 on 2020-01-12 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20200112_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='amount',
            field=models.CharField(choices=[('100 Rupees', '100 Rupees')], max_length=100),
        ),
    ]