# Generated by Django 4.2.4 on 2023-08-17 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtys', '0002_realtymanager'),
    ]

    operations = [
        migrations.CreateModel(
            name='Realty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('s', models.DecimalField(decimal_places=8, max_digits=8)),
                ('info', models.TextField()),
                ('image_cover', models.ImageField(upload_to='image_cover')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realtys.realtymanager')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='realtys.realtytype')),
            ],
        ),
    ]
