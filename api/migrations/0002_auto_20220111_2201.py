# Generated by Django 3.0.8 on 2022-01-11 18:01

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='user_data',
            name='date_of_data',
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='user_data',
            name='types_of_data',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user_data',
            name='value',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='user_data',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
    ]
