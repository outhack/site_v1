from django.forms import ModelForm
from consumer.models import Consumer, Datapoint
# from django.forms.extras.widgets import SelectDateWidget
from django import forms
import datetime
from django.forms import extras
from django.contrib.admin import widgets

class ConsumerForm(ModelForm):
    class Meta:
        model = Consumer
        fields = ['first_name','last_name','gender','dob','ssn','address1','address2','country','city','state','zip_code']

# class DatapointForm()

class ConsumerDatapointForm(forms.Form):
    # your_name = forms.CharField(label='Your name', max_length=100)
    model = Datapoint
    datapoint_set = Datapoint.objects.all()

    # for dp in datapoint_set:
    #     if dp.answer_type == 'text':
    #         datapoint[forloop.counter]= forms.CharField(label=dp.datapoint, )
