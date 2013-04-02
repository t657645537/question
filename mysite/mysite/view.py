#!/usr/bin/python
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
import datetime
import django.template
import books

def current_datetime(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    t = django.template.loader.get_template('test.html')
    html = t.render(django.template.Context({"current_date":now}))
    return HttpResponse(html)
	
def _home(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print request
    t = django.template.loader.get_template('home.html')
    html = t.render(django.template.Context({"current_date":now}))
    return HttpResponse(html)
