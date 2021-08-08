# Generated by Django 3.1 on 2021-06-10 05:34

from django.db import migrations, models
import utils.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210610_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(blank=True, default='avatar/__default__.png', null=True, upload_to=utils.file_upload.FileUploadUtils._wrapper),
        ),
    ]