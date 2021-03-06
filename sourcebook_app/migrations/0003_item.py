# Generated by Django 2.0.5 on 2018-05-09 19:09

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sourcebook_app', '0002_auto_20180506_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('category', models.CharField(max_length=200, null=True)),
                ('source', models.CharField(max_length=200, null=True)),
                ('file', models.FileField(upload_to='media/')),
                ('essay', ckeditor.fields.RichTextField(blank=True)),
            ],
        ),
    ]
