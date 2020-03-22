# Generated by Django 3.0.3 on 2020-03-12 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureHealth', '0027_leavedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='leaveDatas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20)),
                ('employee_role', models.CharField(max_length=20)),
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
        migrations.DeleteModel(
            name='leaveData',
        ),
    ]