# Generated by Django 2.1.1 on 2018-12-10 08:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userss', '0006_remove_joborder_content_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='joborder',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
