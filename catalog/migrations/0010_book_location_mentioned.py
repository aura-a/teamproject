# Generated by Django 2.0.3 on 2018-03-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0009_auto_20180328_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='location_mentioned',
            field=models.CharField(help_text='Where does the action take place.', max_length=1000, null=True),
        ),
    ]
