# Generated by Django 4.0.3 on 2022-04-11 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproducts', '0004_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='addtocart',
            name='is_payment_done',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]