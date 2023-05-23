# Generated by Django 4.2 on 2023-05-06 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_projet_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='projet',
            field=models.ManyToManyField(through='user.detail', to='user.projet'),
        ),
        migrations.AlterField(
            model_name='service',
            name='type',
            field=models.CharField(choices=[('cg', 'Charte graphique '), ('ob', 'Objet  3D'), ('Sc', 'Scénarisation')], default='em', max_length=2),
        ),
    ]