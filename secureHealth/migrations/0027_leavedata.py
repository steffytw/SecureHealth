# Generated by Django 3.0.3 on 2020-03-12 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureHealth', '0026_auto_20200312_0543'),
    ]

    operations = [
        migrations.CreateModel(
            name='leaveData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(max_length=20)),
                ('leave_from', models.DateField()),
                ('leave_to', models.DateField()),
                ('number_of_days', models.IntegerField()),
                ('remaining_leaves', models.IntegerField()),
                ('leave_reason', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Leave Record',
            },
        ),
    ]