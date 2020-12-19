# Generated by Django 3.1 on 2020-11-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningLevel', '0002_homework_mdluser'),
    ]

    operations = [
        migrations.CreateModel(
            name='MdlCourse',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('category', models.BigIntegerField()),
                ('sortorder', models.BigIntegerField()),
                ('fullname', models.CharField(max_length=254)),
                ('shortname', models.CharField(max_length=255)),
                ('idnumber', models.CharField(max_length=100)),
                ('summary', models.TextField(blank=True, null=True)),
                ('summaryformat', models.IntegerField()),
                ('format', models.CharField(max_length=21)),
                ('showgrades', models.IntegerField()),
                ('newsitems', models.IntegerField()),
                ('startdate', models.BigIntegerField()),
                ('enddate', models.BigIntegerField()),
                ('relativedatesmode', models.IntegerField()),
                ('marker', models.BigIntegerField()),
                ('maxbytes', models.BigIntegerField()),
                ('legacyfiles', models.SmallIntegerField()),
                ('showreports', models.SmallIntegerField()),
                ('visible', models.IntegerField()),
                ('visibleold', models.IntegerField()),
                ('groupmode', models.SmallIntegerField()),
                ('groupmodeforce', models.SmallIntegerField()),
                ('defaultgroupingid', models.BigIntegerField()),
                ('lang', models.CharField(max_length=30)),
                ('calendartype', models.CharField(max_length=30)),
                ('theme', models.CharField(max_length=50)),
                ('timecreated', models.BigIntegerField()),
                ('timemodified', models.BigIntegerField()),
                ('requested', models.IntegerField()),
                ('enablecompletion', models.IntegerField()),
                ('completionnotify', models.IntegerField()),
                ('cacherev', models.BigIntegerField()),
            ],
            options={
                'db_table': 'mdl_course',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MdlEnrol',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('enrol', models.CharField(max_length=20)),
                ('status', models.BigIntegerField()),
                ('courseid', models.BigIntegerField()),
                ('sortorder', models.BigIntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('enrolperiod', models.BigIntegerField(blank=True, null=True)),
                ('enrolstartdate', models.BigIntegerField(blank=True, null=True)),
                ('enrolenddate', models.BigIntegerField(blank=True, null=True)),
                ('expirynotify', models.IntegerField(blank=True, null=True)),
                ('expirythreshold', models.BigIntegerField(blank=True, null=True)),
                ('notifyall', models.IntegerField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=50, null=True)),
                ('cost', models.CharField(blank=True, max_length=20, null=True)),
                ('currency', models.CharField(blank=True, max_length=3, null=True)),
                ('roleid', models.BigIntegerField(blank=True, null=True)),
                ('customint1', models.BigIntegerField(blank=True, null=True)),
                ('customint2', models.BigIntegerField(blank=True, null=True)),
                ('customint3', models.BigIntegerField(blank=True, null=True)),
                ('customint4', models.BigIntegerField(blank=True, null=True)),
                ('customint5', models.BigIntegerField(blank=True, null=True)),
                ('customint6', models.BigIntegerField(blank=True, null=True)),
                ('customint7', models.BigIntegerField(blank=True, null=True)),
                ('customint8', models.BigIntegerField(blank=True, null=True)),
                ('customchar1', models.CharField(blank=True, max_length=255, null=True)),
                ('customchar2', models.CharField(blank=True, max_length=255, null=True)),
                ('customchar3', models.CharField(blank=True, max_length=1333, null=True)),
                ('customdec1', models.DecimalField(blank=True, decimal_places=7, max_digits=12, null=True)),
                ('customdec2', models.DecimalField(blank=True, decimal_places=7, max_digits=12, null=True)),
                ('customtext1', models.TextField(blank=True, null=True)),
                ('customtext2', models.TextField(blank=True, null=True)),
                ('customtext3', models.TextField(blank=True, null=True)),
                ('customtext4', models.TextField(blank=True, null=True)),
                ('timecreated', models.BigIntegerField()),
                ('timemodified', models.BigIntegerField()),
            ],
            options={
                'db_table': 'mdl_enrol',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MdlUserEnrolments',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.BigIntegerField()),
                ('enrolid', models.BigIntegerField()),
                ('userid', models.BigIntegerField()),
                ('grade', models.BigIntegerField(blank=True, null=True)),
                ('timestart', models.BigIntegerField()),
                ('timeend', models.BigIntegerField()),
                ('modifierid', models.BigIntegerField()),
                ('timecreated', models.BigIntegerField()),
                ('timemodified', models.BigIntegerField()),
            ],
            options={
                'db_table': 'mdl_user_enrolments',
                'managed': False,
            },
        ),
    ]