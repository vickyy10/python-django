# Generated by Django 5.0.4 on 2024-04-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_member_alter_doctors_doc_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='traill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
            ],
        ),
    ]
