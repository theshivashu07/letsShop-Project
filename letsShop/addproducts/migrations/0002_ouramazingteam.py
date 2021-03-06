# Generated by Django 4.0.3 on 2022-03-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproducts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurAmazingTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_name', models.CharField(max_length=50)),
                ('member_role', models.CharField(max_length=50)),
                ('member_image', models.FileField(default=None, max_length=250, unique=True, upload_to='products/')),
                ('member_instagram_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('member_facebook_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('member_twitter_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('member_linkedin_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('member_github_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
            ],
        ),
    ]
