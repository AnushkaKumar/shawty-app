# Generated by Django 3.0.2 on 2020-01-09 23:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='expiry',
            field=models.IntegerField(default=10000),
        ),
        migrations.AddField(
            model_name='link',
            name='short',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
