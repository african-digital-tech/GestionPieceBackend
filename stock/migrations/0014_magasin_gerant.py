# Generated by Django 4.0.3 on 2022-10-29 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_alter_lignecommande_piece'),
    ]

    operations = [
        migrations.AddField(
            model_name='magasin',
            name='gerant',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='gerant', to='stock.gerant'),
        ),
    ]