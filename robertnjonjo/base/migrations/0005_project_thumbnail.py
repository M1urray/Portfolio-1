# Generated by Django 4.1 on 2022-08-18 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0004_project_alter_post_thumbnail"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                default="/images/placeholder.png",
                null=True,
                upload_to="static/images",
            ),
        ),
    ]
