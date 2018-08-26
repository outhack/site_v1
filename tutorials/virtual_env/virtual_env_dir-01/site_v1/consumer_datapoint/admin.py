# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Account, UserAccount, Consumer, DataPoint, ConsumerDataPoint, DPGroup, DataPointDPGroup

# Register your models here.
admin.site.register(Account)
admin.site.register(UserAccount)
admin.site.register(Consumer)
admin.site.register(DataPoint)
admin.site.register(ConsumerDataPoint)
admin.site.register(DPGroup)
admin.site.register(DataPointDPGroup)
