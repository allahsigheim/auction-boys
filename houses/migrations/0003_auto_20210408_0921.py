# Generated by Django 3.1.7 on 2021-04-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('houses', '0002_auto_20210317_0906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='house',
            options={'ordering': ('auction_date',)},
        ),
        migrations.AddField(
            model_name='house',
            name='street_address',
            field=models.CharField(default='12 boek', max_length=100),
            preserve_default=False,
        ),
    ]
