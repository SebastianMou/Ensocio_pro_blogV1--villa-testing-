# Generated by Django 3.2.6 on 2022-06-29 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_comunicationslinks_pintrist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comunicationslinks',
            old_name='pintrist',
            new_name='pinterest',
        ),
    ]