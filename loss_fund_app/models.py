from django.db import models

# Create your models here.

class police_station(models.Model):
    police_station_id = models.AutoField(primary_key=True,db_column='police_station_id',verbose_name='警局編號')
    police_station_name =  models.CharField(max_length=100,db_column="police_station_name",verbose_name="警局名稱",unique=True)

    class Meta:
        db_table = "police_station"

class police_branch(models.Model):
    police_branch_id = models.AutoField(primary_key=True,db_column='police_branch_id',verbose_name='分局編號')
    police_station_id  = models.ForeignKey(to="police_station",to_field='police_station_id',db_column='police_station_id',verbose_name='所屬警局',on_delete=models.CASCADE)
    police_branch_name =  models.CharField(max_length=100,db_column="police_branch_name",verbose_name="分局名稱",unique=True)

    class Meta:
        db_table = "police_branch"


class local_police_station(models.Model):
    local_police_station_id = models.AutoField(primary_key=True,db_column='local_police_station_id',verbose_name='派出所編號')
    police_branch_id  = models.ForeignKey(to="police_branch",to_field='police_branch_id',db_column='police_branch_id',verbose_name='所屬分局',on_delete=models.CASCADE)
    local_police_station_name =  models.CharField(max_length=100,db_column="local_police_station_name",verbose_name="派出所名稱",unique=True)

    class Meta:
        db_table = "local_police_station"

class loss_funnd_data(models.Model):
    rcno = models.CharField(max_length = 50,primary_key=True)
    police_station_id  = models.ForeignKey(to="police_station",to_field='police_station_id',db_column='police_station_id',verbose_name='受理單位警局',on_delete=models.CASCADE)
    police_branch_id  = models.ForeignKey(to="police_branch",to_field='police_branch_id',db_column='police_branch_id',verbose_name='受理單位分局',on_delete=models.CASCADE)
    local_police_station_id = models.ForeignKey(to="local_police_station",to_field='local_police_station_id',db_column='local_police_station_id',verbose_name='受理單位派出所',on_delete=models.CASCADE)
    datetime = models.DateTimeField(db_column='datetime')
    place = models.CharField(max_length = 150,db_column='place')
    content = models.CharField(max_length = 255,db_column='content',null=True,blank=True)

    class Meta:
        db_table = "loss_funnd_data"

class Area(models.Model):
    area_id = models.AutoField(primary_key=True,db_column='area_id',verbose_name='縣市編號')
    area_name  = models.CharField(max_length = 10,db_column='area_name',verbose_name='縣市編號')
    
    class Meta:
        db_table = 'Area'

class Area_loss_fund_stat(models.Model):
    area_loss_fund_stat_id =  models.AutoField(primary_key=True,db_column='area_loss_fund_stat_id',verbose_name='統計編號')
    area_id = models.ForeignKey(to="Area",to_field='area_id',db_column='area_id',verbose_name='縣市',on_delete=models.CASCADE)
    content = models.CharField(max_length = 255,db_column='content',null=True,blank=True)
    datetime = models.DateTimeField(db_column='datetime')
    class Meta:
        db_table = 'Area_loss_fund_stat'