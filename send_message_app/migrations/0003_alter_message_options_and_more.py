# Generated by Django 4.0.4 on 2022-06-02 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('send_message_app', '0002_alter_client_operator_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ('id', 'status')},
        ),
        migrations.RenameField(
            model_name='message',
            old_name='client_id',
            new_name='client',
        ),
        migrations.RemoveField(
            model_name='message',
            name='mailing_id',
        ),
        migrations.AddField(
            model_name='message',
            name='mailing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='message', to='send_message_app.mailing'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='client',
            name='operator_code',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
    ]
