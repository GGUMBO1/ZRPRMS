# Generated by Django 3.1.5 on 2021-05-25 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvoiceNumber', models.CharField(max_length=20)),
                ('FullName', models.CharField(max_length=200)),
                ('LicenceNumber', models.CharField(max_length=40)),
                ('CarLicence', models.CharField(max_length=50)),
                ('Time', models.DateTimeField()),
                ('Amount', models.IntegerField(default=0)),
                ('Level', models.IntegerField(default=0)),
                ('Description', models.TextField()),
            ],
        ),
    ]
