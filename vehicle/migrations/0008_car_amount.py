# Generated by Django 5.1 on 2024-09-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_alter_moto_description_alter_moto_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='amount',
            field=models.IntegerField(default=1000, verbose_name='цена'),
        ),
    ]
