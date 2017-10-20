from django import template
from django.utils.safestring import mark_safe, SafeData
from django.template.defaultfilters import stringfilter

register = template.Library()

def tokenize(value, delimiter):
    """Splits the string based on the delimiter"""
    return value.replace(arg, '')

@register.filter
@stringfilter
def split_as_option(value, splitter=',', autoescape=None):
    list=value.split(splitter)
    for i in list:
        if " " in i:
            # return i
            i.replace(" ","_")
            # # return len(list)
            # # list.remove(i)
    return list
