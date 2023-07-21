# Generated by Django 4.2.1 on 2023-07-21 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_comment_created_date_alter_post_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 21, 9, 44, 25, 845855, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2023, 7, 21, 9, 44, 25, 844838, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]