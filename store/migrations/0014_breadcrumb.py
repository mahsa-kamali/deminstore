# Generated by Django 4.1.7 on 2023-05-08 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_vendor_shop_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breadcrumb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('url', models.CharField(max_length=200)),
            ],
        ),
    ]
