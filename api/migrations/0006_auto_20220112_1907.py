# Generated by Django 3.0.8 on 2022-01-12 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_user_data_date_of_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='value',
            field=models.FloatField(),
        ),
    ]
