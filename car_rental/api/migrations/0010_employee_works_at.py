# Generated by Django 4.1.2 on 2022-10-14 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rental'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='works_at',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='api.branch'),
            preserve_default=False,
        ),
    ]
