# Generated by Django 4.2.2 on 2023-06-27 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user_f5f96fa1-0d76-40fb-9c5f-4090c704b76a', max_length=150, unique=True),
        ),
    ]