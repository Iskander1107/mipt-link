# Generated by Django 4.2.2 on 2023-06-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='created_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
