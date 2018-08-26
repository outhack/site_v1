# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from fernet_fields import EncryptedTextField
from django_localflavor_us.models import USStateField

# Create your models here.
class Account(models.Model):
    account_name = models.CharField(max_length=64)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField('date joined')
    license_expires = models.DateTimeField('license expires')
    def __str__(self):
        return self.account_name

class UserAccount(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    user_is_account_admin = models.BooleanField(default=False)
    def __str_(self):
        return self.id

class Consumer(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    ssn = EncryptedTextField()
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    date_of_birth = models.DateTimeField('date of birth')
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address1 =  models.CharField(("address1"), max_length=128)
    address2 =  models.CharField(("address2"), max_length=128, blank=True)
    city = models.CharField(("city"), max_length=64)
    state = USStateField(("state"))
    zip_code = models.CharField(("zip code"), max_length=5)
    def __str_(self):
        return (self.last_name+" "+self.first_name)

class DataPoint(models.Model):
    ANSWER_TYPE_CHOICES = (
        ('T', 'Text'),
        ('R', 'Radio'),
        ('D', 'DropDown'),
        ('C', 'Checkbox'),
    )
    datapoint = models.CharField(max_length=1028)
    answer_type = models.CharField(max_length=1, choices=ANSWER_TYPE_CHOICES)
    options = models.CharField(max_length=1028)
    def __str_(self):
        return self.datapoint

class ConsumerDataPoint(models.Model):
    consumer_id = models.ForeignKey(Consumer, on_delete=models.CASCADE)
    datapoint_id = models.ForeignKey(DataPoint, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name="created_by", on_delete=models.CASCADE)
    last_modified_by = models.ForeignKey(User, related_name="last_modified_by",on_delete=models.CASCADE)
    answer = models.CharField(max_length=512)
    remark = models.CharField(max_length=512)
    created_date_time = models.DateTimeField('created date time')
    last_modified_date_time = models.DateTimeField('last modified date time')
    def __str_(self):
        return (self.consumer_id+"- "+self.datapoint_id+": "+self.answer)

class DPGroup(models.Model):
    datapoint_id = models.ForeignKey(DataPoint, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=64)
    def __str_(self):
        return self.group_name

class DataPointDPGroup(models.Model):
    dp_group_id = models.ForeignKey(DPGroup, on_delete=models.CASCADE)
    datapoint_id = models.ForeignKey(DataPoint, on_delete=models.CASCADE)
    def __str_(self):
        return (self.id+" "+self.db_group_id)
