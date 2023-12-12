# Generated by Django 4.2.3 on 2023-07-26 11:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0004_alter_userprofile_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='userID',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
