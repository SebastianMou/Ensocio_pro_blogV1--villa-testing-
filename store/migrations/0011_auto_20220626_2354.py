# Generated by Django 3.2.6 on 2022-06-26 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_comunicationslinks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comunicationslinks',
            name='blog',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comunicationslinks',
            name='facebook',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comunicationslinks',
            name='instagram',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='comunicationslinks',
            name='whatsapp',
            field=models.URLField(max_length=255, null=True),
        ),
    ]