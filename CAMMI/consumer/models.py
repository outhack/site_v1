from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from localflavor.us.us_states import STATE_CHOICES
from localflavor.us.models import USStateField

# Create your models here.

class Account(models.Model):
    account_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField()

class AccountUser(models.Model):
    account_id = models.ForeignKey(User)
    is_account_admin = models.BooleanField(default=False)
    license_expires = models.DateTimeField()

class Consumer(models.Model):
    ssn = models.CharField(max_length=9)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateTimeField()
    GENDER_CHOICES = (('M', 'Male'),('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    address1 = models.CharField(max_length=128)
    address2 = models.CharField(max_length=128, blank=True)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=64)
    state = USStateField(choices = STATE_CHOICES, default='state')
    zip_code = models.CharField( max_length=5)

class Datapoint(models.Model):
    datapoint = models.CharField(max_length=256)
    answer_type = models.CharField(max_length=20) #text, checkbox, radio, select,
    options = models.CharField(max_length=2048)

class Profile(models.Model):
    class Meta:
        unique_together = (('consumer_id','datapoint_id'),)

    consumer_id = models.ForeignKey(Consumer)
    datapoint_id = models.ForeignKey(Datapoint)
    answer = models.CharField(max_length=128)
    remark = models.CharField(max_length=512)
    created_time = models.DateTimeField()
    created_by = models.ForeignKey(User)
    last_modified = models.DateTimeField()
    last_modified_by = models.CharField(max_length=30)

# class Question(models.Model):
#     question_text = models.CharField(max_length=500)
#     published_date = models.DateTimeField('date published')
#     def __str__(self):
#         return self.question_text
