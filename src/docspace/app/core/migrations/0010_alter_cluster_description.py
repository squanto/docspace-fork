# Generated by Django 3.2.14 on 2022-12-11 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_chunk_cluster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cluster',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]