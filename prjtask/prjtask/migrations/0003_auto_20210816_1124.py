# Generated by Django 3.2.2 on 2021-08-16 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prjtask', '0002_alter_user_userlevels'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='end',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='not_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='start',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='projects',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='projects',
            name='status2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='task',
            name='status2',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
