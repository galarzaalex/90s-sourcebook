# Generated by Django 2.0.5 on 2018-05-06 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcebook_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rsvp',
            name='email',
            field=models.EmailField(max_length=200, null=True),
        ),
    ]
