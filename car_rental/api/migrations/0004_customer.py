# Generated by Django 4.1.1 on 2022-10-07 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_employee_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('drivers_license', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=200)),
                ('DOB', models.DateField()),
                ('gold_member', models.BooleanField()),
                ('province', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('postal_code', models.CharField(max_length=6)),
                ('street_number', models.CharField(max_length=10)),
                ('street_name', models.CharField(max_length=30)),
                ('unit_number', models.CharField(max_length=5)),
            ],
        ),
    ]
