# Generated by Django 4.1.7 on 2023-12-12 14:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0002_alter_receipt_date_uploaded"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="company",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="client",
            name="is_representative",
            field=models.BooleanField(default=False),
        ),
    ]