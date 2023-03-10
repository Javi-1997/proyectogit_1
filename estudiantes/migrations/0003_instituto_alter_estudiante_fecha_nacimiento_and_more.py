# Generated by Django 4.1.4 on 2023-01-04 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("estudiantes", "0002_rename_estudiantes_estudiante"),
    ]

    operations = [
        migrations.CreateModel(
            name="Instituto",
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
                ("nombre", models.CharField(max_length=256)),
            ],
        ),
        migrations.AlterField(
            model_name="estudiante",
            name="fecha_nacimiento",
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name="profesor",
            name="bio",
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name="profesor",
            name="fecha_nacimiento",
            field=models.DateField(null=True),
        ),
    ]
