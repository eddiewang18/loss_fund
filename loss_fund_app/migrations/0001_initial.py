# Generated by Django 4.2.4 on 2023-08-24 02:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(db_column='area_id', primary_key=True, serialize=False, verbose_name='縣市編號')),
                ('area_name', models.CharField(db_column='area_name', max_length=10, verbose_name='縣市編號')),
            ],
            options={
                'db_table': 'Area',
            },
        ),
        migrations.CreateModel(
            name='local_police_station',
            fields=[
                ('local_police_station_id', models.AutoField(db_column='local_police_station_id', primary_key=True, serialize=False, verbose_name='派出所編號')),
                ('local_police_station_name', models.CharField(db_column='local_police_station_name', max_length=100, unique=True, verbose_name='派出所名稱')),
            ],
            options={
                'db_table': 'local_police_station',
            },
        ),
        migrations.CreateModel(
            name='police_station',
            fields=[
                ('police_station_id', models.AutoField(db_column='police_station_id', primary_key=True, serialize=False, verbose_name='警局編號')),
                ('police_station_name', models.CharField(db_column='police_station_name', max_length=100, unique=True, verbose_name='警局名稱')),
            ],
            options={
                'db_table': 'police_station',
            },
        ),
        migrations.CreateModel(
            name='police_branch',
            fields=[
                ('police_branch_id', models.AutoField(db_column='police_branch_id', primary_key=True, serialize=False, verbose_name='分局編號')),
                ('police_branch_name', models.CharField(db_column='police_branch_name', max_length=100, unique=True, verbose_name='分局名稱')),
                ('police_station_id', models.ForeignKey(db_column='police_station_id', on_delete=django.db.models.deletion.CASCADE, to='loss_fund_app.police_station', verbose_name='所屬警局')),
            ],
            options={
                'db_table': 'police_branch',
            },
        ),
        migrations.CreateModel(
            name='loss_funnd_data',
            fields=[
                ('rcno', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField(db_column='datetime')),
                ('place', models.CharField(db_column='place', max_length=150)),
                ('content', models.CharField(blank=True, db_column='content', max_length=255, null=True)),
                ('local_police_station_id', models.ForeignKey(db_column='local_police_station_id', on_delete=django.db.models.deletion.CASCADE, to='loss_fund_app.local_police_station', verbose_name='受理單位派出所')),
                ('police_branch_id', models.ForeignKey(db_column='police_branch_id', on_delete=django.db.models.deletion.CASCADE, to='loss_fund_app.police_branch', verbose_name='受理單位分局')),
                ('police_station_id', models.ForeignKey(db_column='police_station_id', on_delete=django.db.models.deletion.CASCADE, to='loss_fund_app.police_station', verbose_name='受理單位警局')),
            ],
            options={
                'db_table': 'loss_funnd_data',
            },
        ),
        migrations.AddField(
            model_name='local_police_station',
            name='police_branch_id',
            field=models.ForeignKey(db_column='police_branch_id', on_delete=django.db.models.deletion.CASCADE, to='loss_fund_app.police_branch', verbose_name='所屬分局'),
        ),
        migrations.CreateModel(
            name='Area_loss_fund_stat',
            fields=[
                ('area_loss_fund_stat_id', models.AutoField(db_column='area_loss_fund_stat_id', primary_key=True, serialize=False, verbose_name='統計編號')),
                ('content', models.CharField(blank=True, db_column='content', max_length=255, null=True)),
                ('datetime', models.DateTimeField(db_column='datetime')),
                ('area_id', models.ForeignKey(db_column='area_id', on_delete=django.db.models.deletion.CASCADE, to='loss_fund_app.area', verbose_name='縣市')),
            ],
            options={
                'db_table': 'Area_loss_fund_stat',
            },
        ),
    ]