# Generated by Django 4.2 on 2023-05-01 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('Charte graphique', ': Charte graphique '), ('Objet  3D', 'Objet  3D'), ('Scénarisation', 'Scénarisation')], default='em', max_length=20),
        ),
    ]
