# Generated by Django 5.1.6 on 2025-02-27 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('joinbackend_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['firstName']},
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='last_name',
            new_name='lastName',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='phone_number',
            new_name='phoneNumber',
        ),
    ]
