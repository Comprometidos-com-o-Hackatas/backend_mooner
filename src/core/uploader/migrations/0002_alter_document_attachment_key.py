# Generated by Django 5.0.7 on 2024-10-29 16:15

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploader', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='attachment_key',
            field=models.CharField(default=uuid.uuid4, help_text='Used to attach the document to another object. Cannot be used to retrieve the document file.', max_length=255, unique=True),
        ),
    ]