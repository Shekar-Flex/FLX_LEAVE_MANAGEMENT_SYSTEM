# Generated by Django 4.0.4 on 2022-05-11 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavedata',
            name='reasontype',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
