# Generated by Django 3.0.8 on 2020-07-09 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20200708_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='contacts.Contact'),
        ),
    ]
