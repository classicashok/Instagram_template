# Generated by Django 2.2 on 2019-12-22 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermodel',
            name='bio',
            field=models.TextField(default='this is default bio', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]