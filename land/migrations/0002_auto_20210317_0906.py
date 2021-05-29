# Generated by Django 3.1.7 on 2021-03-17 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('land', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='land',
            name='main_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='land',
            name='start_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=12),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Extra_Images_Land',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('land', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='land.land', verbose_name='Land')),
            ],
        ),
    ]
