# Generated by Django 3.1.7 on 2021-06-02 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ECOMMERCE', '0007_customerorder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='status',
            new_name='active',
        ),
    ]