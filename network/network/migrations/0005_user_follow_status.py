# Generated by Django 3.2.2 on 2021-07-15 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_auto_20210714_1930'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='follow_status',
            field=models.BooleanField(default=False),
        ),
    ]