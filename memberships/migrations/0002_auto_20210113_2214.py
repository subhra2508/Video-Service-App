# Generated by Django 3.1.5 on 2021-01-13 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subscription',
            old_name='strip_subscription_id',
            new_name='stripe_subscription_id',
        ),
        migrations.RenameField(
            model_name='usermembership',
            old_name='strip_customer_id',
            new_name='stripe_customer_id',
        ),
    ]
