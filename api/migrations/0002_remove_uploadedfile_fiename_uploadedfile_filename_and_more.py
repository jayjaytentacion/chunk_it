# Generated by Django 4.0.6 on 2022-07-27 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadedfile',
            name='fiename',
        ),
        migrations.AddField(
            model_name='uploadedfile',
            name='filename',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='uploadedfile',
            name='cutomuser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
