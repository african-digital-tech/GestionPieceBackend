# Generated by Django 4.1.1 on 2022-11-02 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0015_alter_commandefournisseur_numcommande"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commandefournisseur",
            name="numCommande",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]
