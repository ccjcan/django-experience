# Generated by Django 4.0 on 2022-02-28 22:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.user'),
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('p', 'Pendente'), ('a', 'Aprovado'), ('c', 'Cancelado')], default='p', max_length=1),
        ),
    ]