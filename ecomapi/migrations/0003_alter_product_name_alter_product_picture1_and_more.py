# Generated by Django 4.1.1 on 2022-09-08 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomapi', '0002_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture1',
            field=models.ImageField(max_length=254, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='product',
            name='picture2',
            field=models.ImageField(max_length=254, upload_to='photos'),
        ),
    ]
