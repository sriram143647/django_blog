# Generated by Django 4.2.9 on 2024-01-12 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_users', '0004_alter_bloguser_contact_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='is_confirmed',
            field=models.BooleanField(default=False),
        ),
    ]
