# Generated by Django 3.1 on 2021-06-15 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problem', '0002_rename_tagname_problemtag_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='visible',
            field=models.BooleanField(default=True, null=True),
        ),
    ]