# Generated by Django 3.2 on 2021-06-27 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.adminuser'),
        ),
    ]
