# Generated by Django 3.1.7 on 2021-04-08 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0002_auto_20210317_0906'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='land',
            options={'ordering': ('auction_date',), 'verbose_name_plural': 'Land'},
        ),
        migrations.AddField(
            model_name='land',
            name='street_address',
            field=models.CharField(default='This is adress boii', max_length=100),
            preserve_default=False,
        ),
    ]
