# Generated by Django 4.2 on 2023-05-13 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_equipe_projet_remove_personnel_equipe_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipe',
            old_name='personnel',
            new_name='personnels',
        ),
    ]
