# Generated by Django 5.0.7 on 2024-09-22 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooner', '0004_remove_lunaai_response'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunaai',
            name='response',
            field=models.TextField(blank=True, null=True),
        ),
    ]
