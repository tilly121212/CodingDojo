# Generated by Django 2.2 on 2020-11-18 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('course_app', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ManyToManyField(related_name='courses', to='login_app.User'),
        ),
    ]
