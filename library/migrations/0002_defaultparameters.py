# Generated by Django 2.2.6 on 2019-10-30 19:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultParameters',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the default parameters ', primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('default_rate', models.CharField(max_length=100)),
                ('default_months', models.CharField(max_length=200)),
                ('default_principal', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Default Values',
                'verbose_name_plural': 'Default Values',
            },
        ),
    ]
