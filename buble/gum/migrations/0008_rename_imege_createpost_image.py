# Generated by Django 4.0.3 on 2022-04-17 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gum', '0007_alter_createpost_options_createpost_imege'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createpost',
            old_name='imege',
            new_name='image',
        ),
    ]