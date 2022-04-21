# Generated by Django 4.0 on 2022-04-21 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auditorium', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reserved', models.BooleanField(default=True)),
                ('paid', models.BooleanField(default=False)),
                ('active', models.BooleanField(default=None)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.useraccount')),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auditorium.screening')),
            ],
        ),
        migrations.CreateModel(
            name='SeatReserved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='reservation.reservation')),
                ('screening', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auditorium.screening')),
                ('seat', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='auditorium.seat')),
            ],
        ),
    ]
