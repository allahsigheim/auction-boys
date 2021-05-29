# Generated by Django 3.1.7 on 2021-03-12 10:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Townhouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('living_rooms', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bath_rooms', models.IntegerField()),
                ('garages', models.IntegerField()),
                ('under_roof_sqm', models.IntegerField()),
                ('rates_taxes', models.IntegerField()),
                ('levis', models.IntegerField()),
                ('carport', models.IntegerField()),
                ('security', models.CharField(max_length=100)),
                ('yard_space', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('laundry', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('pool', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=20)),
                ('fibre', models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20, null=True)),
                ('full_or_sectional', models.CharField(choices=[('Full Title Town House', 'Full Title Town House'), ('Sectional Title Town House', 'Sectional Title Town House')], default='Full Title Town House', max_length=100)),
                ('auction_date', models.DateTimeField()),
                ('province', models.CharField(choices=[('Eastern Cape', 'Eastern Cape'), ('Freestate', 'Freestate'), ('Gauteng', 'Gauteng'), ('Kwazulu-Natal', 'Kwazulu-Natal'), ('Limpopo', 'Limpopo'), ('Mpumulanga', 'Mpumulanga'), ('North West', 'North West'), ('Northen Cape', 'Northen Cape'), ('Western Cape', 'Western Cape')], max_length=20)),
                ('town_or_city', models.CharField(max_length=100)),
                ('agent_name', models.CharField(max_length=50)),
                ('agent_email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.agent', to_field='email')),
            ],
        ),
    ]
