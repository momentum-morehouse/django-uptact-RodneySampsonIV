# Generated by Django 3.0.8 on 2020-07-08 15:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_birthday'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('nickname', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=11, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999-999-9999'.", regex='^\\+?\\d{10}$')]),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Contact')),
            ],
        ),
    ]
