# Generated by Django 4.2.4 on 2023-09-01 07:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="author",
            name="is_blocked",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="post",
            name="author",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="author_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
