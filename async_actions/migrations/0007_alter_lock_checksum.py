# Generated by Django 4.2.4 on 2023-10-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('async_actions', '0006_remove_actiontaskstate_async_actio_active_5f7c81_idx_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lock',
            name='checksum',
            field=models.CharField(max_length=24, unique=True, verbose_name='Checksum'),
        ),
    ]
