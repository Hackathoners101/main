# Generated by Django 3.2 on 2023-04-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0003_alter_member_expirience'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/'),
        ),
    ]
