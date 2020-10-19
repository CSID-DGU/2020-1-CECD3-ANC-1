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

class MdlEnrolFlatfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=30)
    roleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    coursename = models.CharField(max_length=100, blank=True, null=True)
    grade = models.BigIntegerField(blank=True, null=True)
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol_flatfile'


class MdlUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    auth = models.CharField(max_length=20)
    confirmed = models.IntegerField()
    policyagreed = models.IntegerField()
    deleted = models.IntegerField()
    suspended = models.IntegerField()
    mnethostid = models.BigIntegerField()
    username = models.CharField(max_length=100)
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
        managed = False
        db_table = 'mdl_user'
        unique_together = (('mnethostid', 'username'),)


class MdlRoleAssignments(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemid = models.BigIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_role_assignments'


class MdlCourseSections(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    section = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.IntegerField()
    sequence = models.TextField(blank=True, null=True)
    visible = models.IntegerField()
    availability = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_course_sections'
        unique_together = (('course', 'section'),)


class SComment(models.Model):
    userid = models.IntegerField(blank=True, null=True)
    q_id = models.IntegerField(blank=True, null=True)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    like = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 's_comment'


class MdlUserEnrolments(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.BigIntegerField()
    enrolid = models.BigIntegerField()
    userid = models.BigIntegerField()
    grade = models.BigIntegerField(blank=True, null=True)
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_user_enrolments'
        unique_together = (('enrolid', 'userid'),)


class MdlEnrol(models.Model):
    id = models.BigAutoField(primary_key=True)
    enrol = models.CharField(max_length=20)
    status = models.BigIntegerField()
    courseid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    enrolperiod = models.BigIntegerField(blank=True, null=True)
    enrolstartdate = models.BigIntegerField(blank=True, null=True)
    enrolenddate = models.BigIntegerField(blank=True, null=True)
    expirynotify = models.IntegerField(blank=True, null=True)
    expirythreshold = models.BigIntegerField(blank=True, null=True)
    notifyall = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    cost = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    roleid = models.BigIntegerField(blank=True, null=True)
    customint1 = models.BigIntegerField(blank=True, null=True)
    customint2 = models.BigIntegerField(blank=True, null=True)
    customint3 = models.BigIntegerField(blank=True, null=True)
    customint4 = models.BigIntegerField(blank=True, null=True)
    customint5 = models.BigIntegerField(blank=True, null=True)
    customint6 = models.BigIntegerField(blank=True, null=True)
    customint7 = models.BigIntegerField(blank=True, null=True)
    customint8 = models.BigIntegerField(blank=True, null=True)
    customchar1 = models.CharField(max_length=255, blank=True, null=True)
    customchar2 = models.CharField(max_length=255, blank=True, null=True)
    customchar3 = models.CharField(max_length=1333, blank=True, null=True)
    customdec1 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customdec2 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customtext1 = models.TextField(blank=True, null=True)
    customtext2 = models.TextField(blank=True, null=True)
    customtext3 = models.TextField(blank=True, null=True)
    customtext4 = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_enrol'


class MdlCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.IntegerField()
    format = models.CharField(max_length=21)
    showgrades = models.IntegerField()
    newsitems = models.IntegerField()
    startdate = models.BigIntegerField()
    enddate = models.BigIntegerField()
    relativedatesmode = models.IntegerField()
    marker = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    legacyfiles = models.SmallIntegerField()
    showreports = models.SmallIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    groupmode = models.SmallIntegerField()
    groupmodeforce = models.SmallIntegerField()
    defaultgroupingid = models.BigIntegerField()
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requested = models.IntegerField()
    enablecompletion = models.IntegerField()
    completionnotify = models.IntegerField()
    cacherev = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mdl_course'
