# Generated by Django 3.1.5 on 2021-09-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loanApp', '0002_auto_20210903_1057'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanrequest',
            name='year',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
