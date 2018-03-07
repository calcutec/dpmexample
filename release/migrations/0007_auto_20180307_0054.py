# Generated by Django 2.0.2 on 2018-03-07 00:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('release', '0006_auto_20180307_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_number', models.IntegerField(choices=[('ONE', 1), ('TWO', 2), ('THREE', 3), ('FOUR', 4)], default='ONE', max_length=2)),
                ('bt_compilation', models.NullBooleanField()),
                ('release', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='release.Release')),
            ],
        ),
        migrations.RemoveField(
            model_name='track',
            name='disc_no',
        ),
    ]