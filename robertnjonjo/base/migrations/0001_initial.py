# Generated by Django 4.1 on 2022-08-15 07:55

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("headline", models.CharField(max_length=200)),
                (
                    "sub_headline",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "thumbnail",
                    models.ImageField(
                        blank=True,
                        default="/images/placeholder.png",
                        null=True,
                        upload_to="images",
                    ),
                ),
                (
                    "body",
                    ckeditor_uploader.fields.RichTextUploadingField(
                        blank=True, null=True
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("active", models.BooleanField(default=False)),
                ("featured", models.BooleanField(default=False)),
                ("tags", models.ManyToManyField(blank=True, null=True, to="base.tag")),
            ],
        ),
    ]
