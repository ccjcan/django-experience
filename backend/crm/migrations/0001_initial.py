# Generated by Django 4.0.3 on 2022-03-30 01:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg', models.CharField(blank=True, max_length=10, null=True)),
                ('cpf', models.CharField(blank=True, max_length=11, null=True)),
                ('cep', models.CharField(blank=True, max_length=8, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('active', models.BooleanField(default=True)),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller_customers', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cliente',
                'verbose_name_plural': 'clientes',
                'ordering': ('user__first_name',),
            },
        ),
        migrations.CreateModel(
            name='Comission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comissions', to='auth.group')),
            ],
            options={
                'verbose_name': 'comissão',
                'verbose_name_plural': 'comissões',
                'ordering': ('group__name',),
            },
        ),
    ]
