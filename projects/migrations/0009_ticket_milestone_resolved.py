# Generated by Django 4.0.4 on 2022-06-24 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_ticket_sprint'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='milestone_resolved',
            field=models.IntegerField(default=0),
        ),
    ]
