# Generated by Django 4.1.1 on 2022-11-04 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0020_alter_commandefournisseur_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="commandefournisseur",
            name="numCommande",
            field=models.CharField(max_length=250, null=True, unique=True),
        ),
    ]
