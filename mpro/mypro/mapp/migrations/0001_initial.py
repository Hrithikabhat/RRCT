# Generated by Django 4.2 on 2023-04-27 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="patientid",
            fields=[
                ("img", models.ImageField(upload_to="../static/assests")),
                (
                    "gender",
                    models.CharField(
                        choices=[
                            ("SELECT", "SELECT"),
                            ("MALE", "MALE"),
                            ("FEMALE", "FEMALE"),
                        ],
                        default="SELECT",
                        max_length=6,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("TYPE", "TYPE"),
                            ("BLOOD CANCER", "BLOOD CANCER"),
                            ("BREAST CANCER", "BREAST CANCER"),
                            ("LUNG CANCER", "LUNG CANCER"),
                            ("PROSTATE CANCER", "PROSTATE CANCER"),
                            ("SKIN CANCER", "SKIN CANCER"),
                        ],
                        default="TYPE",
                        max_length=16,
                    ),
                ),
                (
                    "stage",
                    models.CharField(
                        choices=[
                            ("STAGE", "STAGE"),
                            ("0", "0"),
                            ("1", "1"),
                            ("2", "2"),
                            ("3", "3"),
                            ("4", "4"),
                        ],
                        default="STAGE",
                        max_length=6,
                    ),
                ),
                (
                    "id",
                    models.IntegerField(
                        max_length=10, primary_key=True, serialize=False, unique=True
                    ),
                ),
                ("first_name", models.CharField(max_length=30)),
                ("last_name", models.CharField(max_length=30)),
                ("age", models.IntegerField(max_length=2)),
                ("email", models.EmailField(max_length=40)),
                ("phone", models.IntegerField(max_length=10)),
                ("address_a", models.TextField(max_length=60)),
                ("address_b", models.TextField(max_length=60)),
            ],
        ),
    ]