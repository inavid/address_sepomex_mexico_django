# Generated by Django 2.1.7 on 2019-07-22 19:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sepomex', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('postal_code', models.CharField(max_length=5)),
                ('street', models.CharField(max_length=100)),
                ('external_number', models.CharField(max_length=100)),
                ('internal_number', models.CharField(blank=True, max_length=100, null=True)),
                ('is_active', models.BooleanField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('sepomex', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sepomex.Sepomex')),
            ],
        ),
    ]
