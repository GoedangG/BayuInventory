# Generated by Django 4.2.5 on 2023-09-26 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='amount',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]