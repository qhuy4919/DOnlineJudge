# Generated by Django 3.2.5 on 2021-07-22 08:02

from django.db import migrations, models
import utils.file_upload


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0007_alter_problem_test_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='test_zip',
            field=models.FileField(blank=True, default=None, null=True, upload_to=utils.file_upload.FileUploadUtils._wrapper),
        ),
    ]