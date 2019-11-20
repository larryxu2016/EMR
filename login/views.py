from django.http import HttpResponse
from django.shortcuts import render
from .models import PatientLogin

# Create your views here.
def index(request):
    return render(request, "login/index.html")

def newUser(request): 
    return render(request, "login/newUser.html")

def changePwdPage(request):
    if request.session.get('member_id'):
        return render(request, "login/changepwd.html")
    return render(request, "login/index.html")  
    
def login(request):
    users = PatientLogin.objects.all() \
            .filter(user_name__exact = request.POST['user'], password__exact = request.POST['pwd']).values();
    if users.count() != 1:  
        return HttpResponse("error")
    request.session['member_id'] = request.POST['user']
    request.session.set_expiry(180)
    return HttpResponse("success")

def changePwd(request):
    if request.session.get('member_id'):   
        users = PatientLogin.objects.get(user_name=request.session.get('member_id'))
        if users.password == request.POST['oldpwd']:
            users.password = request.POST['newpwd']
            users.save()
            return HttpResponse("success")
        else:    
            return HttpResponse("error")     
    else:
        return render(request, "login/index.html")

def createUser(request):
    users = PatientLogin.objects.all() \
            .filter(user_name__exact = request.POST['user']).values();
    if users.count() == 0:
        pl = PatientLogin(
            user_name = request.POST['user'],
            email = request.POST['email'],
            password = request.POST['pwd'])
        pl.save()
        request.session['member_id'] = request.POST['user']
        return HttpResponse("success")
    return HttpResponse("error")

def logoff(request):
    del request.session['member_id']
    request.session.modified = True
    return render(request, "login/index.html")