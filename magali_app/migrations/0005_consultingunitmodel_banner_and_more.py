# Generated by Django 4.2.1 on 2023-05-24 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magali_app', '0004_consultingmodel_consultingunitmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='consultingunitmodel',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='unitfiles/'),
        ),
        migrations.AlterField(
            model_name='consultingmodel',
            name='banner',
            field=models.ImageField(blank=True, null=True, upload_to='consultingfiles/'),
        ),
    ]
