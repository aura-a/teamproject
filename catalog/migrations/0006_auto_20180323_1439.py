# Generated by Django 2.0.3 on 2018-03-23 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_book_quotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quotes',
            field=models.TextField(blank=True, default='', help_text='Enter some quotes from the book.', max_length=2000),
        ),
    ]