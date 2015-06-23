from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.contrib.auth.models import *
# Create your views here.

def index(request):
    context = {}
    return render(request, 'basic/index.html', context)

def landing(request):
    errors = []
    resp = {}
    print request.POST
    _username = request.POST.get('username')
    print _username
    _role = request.POST.get('role')
    print _role
    _password = request.POST.get('password')
    print _password
    #signup
    if _role == 'teacher' or _role == 'student':
        a = User.objects.filter(username=_username)
        # if empty list
        if not a:
            b = User(username=_username, password=_password)
            b.save()
        else:
            errors.append("username already taken")
    else:
        k = User.objects.filter(username=_username)
        pas = k.password
    if errors:
        resp['status'] = 'error'
        resp['errors'] = errors
    else:
        resp['status'] = 'success'
    if resp['status'] == 'success':
        return render_to_response('basic/tests.html',
                {'username':_username}, context_instance = RequestContext(request))
    else:
        return HttpResponse(json.dumps(resp), contect_type='application/json')

