# Generated by Django 4.2.6 on 2024-03-29 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_booking_customer_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canclerequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookingid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.booking')),
            ],
        ),
    ]
