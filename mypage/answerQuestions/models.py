from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Question(models.Model):
    q_id = models.IntegerField(primary_key=True)
    q_c_id = models.IntegerField()
    q_s_id = models.IntegerField()
    q_c_name = models.CharField(max_length=100)
    ch_id = models.IntegerField()
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    satisfaction = models.CharField(max_length=10, blank=True, null=True)
    t_year = models.CharField(max_length=45)
    t_semester = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'question'
        unique_together = (('q_id', 'q_c_id', 't_year', 't_semester'),)
