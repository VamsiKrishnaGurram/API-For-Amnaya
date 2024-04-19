# Generated by Django 4.2.11 on 2024-04-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API_for_Project', '0010_dict_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='Items',
        ),
        migrations.AddField(
            model_name='products',
            name='Items',
            field=models.ManyToManyField(db_index=True, to='API_for_Project.dict'),
        ),
    ]