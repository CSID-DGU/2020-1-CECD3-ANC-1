# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class MdlUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    auth = models.CharField(max_length=20)
    confirmed = models.IntegerField()
    policyagreed = models.IntegerField()
    deleted = models.IntegerField()
    suspended = models.IntegerField()
    mnethostid = models.BigIntegerField()
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    emailstop = models.IntegerField()
    icq = models.CharField(max_length=15)
    skype = models.CharField(max_length=50)
    yahoo = models.CharField(max_length=50)
    aim = models.CharField(max_length=50)
    msn = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    institution = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=2)
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    firstaccess = models.BigIntegerField()
    lastaccess = models.BigIntegerField()
    lastlogin = models.BigIntegerField()
    currentlogin = models.BigIntegerField()
    lastip = models.CharField(max_length=45)
    secret = models.CharField(max_length=15)
    picture = models.BigIntegerField()
    url = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    mailformat = models.IntegerField()
    maildigest = models.IntegerField()
    maildisplay = models.IntegerField()
    autosubscribe = models.IntegerField()
    trackforums = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    trustbitmask = models.BigIntegerField()
    imagealt = models.CharField(max_length=255, blank=True, null=True)
    lastnamephonetic = models.CharField(max_length=255, blank=True, null=True)
    firstnamephonetic = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    alternatename = models.CharField(max_length=255, blank=True, null=True)
    moodlenetprofile = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'mdl_user'
        unique_together = (('mnethostid', 'username'),)


class MdlEnrolFlatfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=30)
    roleid = models.BigIntegerField()
    userid = models.CharField(max_length=100)
    courseid = models.BigIntegerField()
    grade = models.CharField(max_length=45, blank=True, null=True)
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_flatfile'

class HomeWork(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)