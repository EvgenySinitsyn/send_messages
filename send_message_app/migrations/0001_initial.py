# Generated by Django 4.0.4 on 2022-05-31 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('operator_code', models.CharField(max_length=10)),
                ('tag', models.CharField(blank=True, max_length=255)),
                ('timezone', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_datetime', models.DateTimeField()),
                ('text', models.TextField()),
                ('mark', models.CharField(max_length=255)),
                ('end_datetime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('send_datetime', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(max_length=255)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send_message_app.client')),
                ('mailing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='send_message_app.mailing')),
            ],
        ),
    ]