# Generated by Django 2.1.1 on 2019-03-24 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0008_auto_20190324_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]