# Generated by Django 5.1.2 on 2024-11-03 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
