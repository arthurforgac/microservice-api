# Generated by Django 4.0.6 on 2022-07-14 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='userid',
            field=models.PositiveIntegerField(),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
