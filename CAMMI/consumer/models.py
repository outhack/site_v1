from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=500)
    published_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
