# Generated by Django 2.1.1 on 2018-12-08 08:26

import DOCS.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(choices=[('type1', 'TYPE1'), ('type2', 'TYPE2'), ('type3', 'TYPE3'), ('type4', 'TYPE4')], default='Normal', max_length=10)),
                ('Title', models.CharField(max_length=200)),
                ('File', models.FileField(upload_to='Document/files/', validators=[DOCS.validators.validate_file_extension])),
                ('Description', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
            ],
        ),
    ]
