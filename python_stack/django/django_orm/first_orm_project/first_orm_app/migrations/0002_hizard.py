# Generated by Django 2.2 on 2020-10-22 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_orm_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hizard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45)),
                ('house', models.CharField(max_length=45)),
                ('pet', models.CharField(max_length=45)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
