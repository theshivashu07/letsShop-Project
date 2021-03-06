# Generated by Django 4.0.3 on 2022-04-10 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproducts', '0003_addtocart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.CharField(max_length=10)),
                ('addtocart_id', models.CharField(max_length=10)),
                ('product_slug', models.CharField(max_length=50)),
                ('product_quantity', models.CharField(max_length=5)),
                ('payment_total_ammount', models.CharField(max_length=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('is_product_delivered', models.CharField(max_length=5)),
            ],
        ),
    ]
