# Generated by Django 4.2.1 on 2023-07-21 09:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_post_create_date_post_created_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 21, 9, 23, 20, 47887, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 21, 9, 23, 20, 47887, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
