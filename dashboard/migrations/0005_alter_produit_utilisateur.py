# Generated by Django 3.2 on 2021-06-27 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_alter_produit_utilisateur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.adminuser'),
        ),
    ]