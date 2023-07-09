# Generated by Django 4.2.3 on 2023-07-09 09:13

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
            name='Licenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=50)),
                ('jobtitle', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator])),
                ('softwareusername', models.CharField(max_length=50)),
                ('expirationdate', models.DateField()),
                ('version', models.CharField(max_length=50)),
                ('created', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
