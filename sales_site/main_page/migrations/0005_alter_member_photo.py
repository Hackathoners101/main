# Generated by Django 3.2 on 2023-04-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_member_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='C:\\Scripts\\vicroria_project\\Victoria_project\\sales_site\\media'),
        ),
    ]
