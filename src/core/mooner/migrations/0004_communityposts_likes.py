
# Generated by Django 5.1.2 on 2024-11-27 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mooner', '0003_alter_communityposts_songs'),
    ]

    operations = [
        migrations.AddField(
            model_name='communityposts',
            name='likes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
