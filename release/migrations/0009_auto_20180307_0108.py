# Generated by Django 2.0.2 on 2018-03-07 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0008_auto_20180307_0058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='disc',
            old_name='bt_compilation',
            new_name='compilation',
        ),
        migrations.RemoveField(
            model_name='disc',
            name='in_number',
        ),
        migrations.AddField(
            model_name='disc',
            name='number',
            field=models.IntegerField(choices=[(1, 'One'), (2, 'Two'), (3, 'Three'), (4, 'Four')], default=1),
        ),
    ]
