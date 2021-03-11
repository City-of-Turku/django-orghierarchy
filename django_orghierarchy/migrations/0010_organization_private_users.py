# Generated by Django 2.2.11 on 2021-01-04 08:57

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('django_orghierarchy', '0009_add_change_organization_regular_users_permission'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='private_users',
            field=models.ManyToManyField(blank=True, related_name='public_memberships', to=settings.AUTH_USER_MODEL),
        ),
    ]