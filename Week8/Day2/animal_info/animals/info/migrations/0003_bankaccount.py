# Generated by Django 3.2.3 on 2021-05-26 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_animalclimate_passport_person'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.CharField(max_length=10)),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.person')),
            ],
        ),
    ]
