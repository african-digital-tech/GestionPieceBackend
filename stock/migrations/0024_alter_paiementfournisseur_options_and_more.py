# Generated by Django 4.1.1 on 2022-11-04 10:18

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("stock", "0023_alter_magasin_options_alter_magasin_gerant"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="paiementfournisseur",
            options={"ordering": ["id", "montantPaye", "facture", "datePaiement"]},
        ),
        migrations.AddField(
            model_name="paiementfournisseur",
            name="datePaiement",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="facture",
            name="numFacture",
            field=models.CharField(max_length=12, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="quantitéstock",
            name="magasin",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="info_quantite",
                to="stock.magasin",
            ),
        ),
    ]
