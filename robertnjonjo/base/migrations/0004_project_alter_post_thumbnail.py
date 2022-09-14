# Generated by Django 4.1 on 2022-08-18 08:43

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_profile_postcomment"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(blank=True, max_length=400, null=True)),
                (
                    "tasks",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                (
                    "achievements",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                ("slug", models.SlugField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name="post",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                default="/images/placeholder.png",
                null=True,
                upload_to="static/images",
            ),
        ),
    ]
