# Generated by Django 3.2.16 on 2023-01-06 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='sales',
            field=models.IntegerField(verbose_name='销量'),
        ),
    ]
