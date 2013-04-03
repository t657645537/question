#!/usr/bin/python
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.http import HttpResponseRedirect
import datetime
import django.template
import books

def current_datetime(request):
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    t = django.template.loader.get_template('test.html')
    html = t.render(django.template.Context({"current_date":now}))
    return HttpResponse(html)
	
def home(request):
	print request.session.get('username','')
	now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	t = django.template.loader.get_template('home.html')
	html = t.render(django.template.Context({
		"isLogin":request.session.get('isLogin',False),
		"username":request.session.get('username',''),
		"question":books.models.Question.all()
		}))
	return HttpResponse(html)

def login(request):
	return getHtml('login.html')
	
def login_to_home(request):
	uname = request.GET.get('username','')
	pword = request.GET.get('password','')
	
	retval = books.models.User.objects.filter(username=uname,
		password=pword)
	
	if len(retval) == 0:
		request.session['isLogin'] = False
	else:
		request.session['isLogin'] = True
		request.session['username'] = uname
	return HttpResponseRedirect('/home')
	
def logout(request):
	del request.session['isLogin']
	del request.session['username']
	return HttpResponseRedirect('/home')
	
def publish(request):
	return getHtml('publish.html')
	
def getHtml(url):
	t = django.template.loader.get_template(url)
	html = t.render(django.template.Context({}))
	return HttpResponse(html)