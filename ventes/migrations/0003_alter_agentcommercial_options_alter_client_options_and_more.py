# Generated by Django 4.0.3 on 2022-10-29 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ventes', '0002_alter_commandclient_piecevendue_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agentcommercial',
            options={'ordering': ['id', '-date_creation', 'nom_agent', 'prenom_agent', 'email_agent']},
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['id', '-date_creation', 'nom_client', 'prenom_client']},
        ),
        migrations.AlterModelOptions(
            name='commandclient',
            options={'ordering': ['id', '-date_creation', 'numCommande', 'totalCommande']},
        ),
        migrations.AlterModelOptions(
            name='factureclient',
            options={'ordering': ['id', '-date_creation', 'numFacture']},
        ),
        migrations.AlterModelOptions(
            name='infoscommandeclient',
            options={'ordering': ['id', '-date_creation', 'quantite', 'prix_unitaire']},
        ),
        migrations.AlterModelOptions(
            name='paiement',
            options={'ordering': ['id', '-date_creation', 'montant']},
        ),
    ]
