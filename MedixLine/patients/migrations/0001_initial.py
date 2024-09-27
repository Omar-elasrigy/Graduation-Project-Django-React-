# Generated by Django 4.2.16 on 2024-09-27 12:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10)),
                ('phone_number', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(message='Not A Valid Phone Number.', regex='^(010|011|015|012)\\d{8}$')])),
                ('address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
