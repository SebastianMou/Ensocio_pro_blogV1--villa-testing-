# Generated by Django 3.2.6 on 2022-06-19 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='video',
            field=models.URLField(default='sebastian', max_length=300, null=True),
        ),
    ]
