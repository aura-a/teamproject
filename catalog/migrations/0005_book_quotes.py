# Generated by Django 2.0.3 on 2018-03-23 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_location_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quotes',
            field=models.TextField(default='', help_text='Enter some quotes from the book.', max_length=2000),
        ),
    ]