# Generated by Django 5.1 on 2024-08-15 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_user_userpassword'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='inv',
            field=models.CharField(default='', max_length=10000000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='money',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
