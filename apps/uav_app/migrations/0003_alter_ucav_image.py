# Generated by Django 5.0 on 2023-12-09 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uav_app', '0002_alter_aircraftcategory_options_alter_ucav_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ucav',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/ucavs/%Y/%m/'),
        ),
    ]
