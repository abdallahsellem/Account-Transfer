# Generated by Django 4.2.13 on 2024-05-17 09:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('owner_name', models.CharField(max_length=256)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
