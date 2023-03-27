from django.shortcuts import render

# Create your views here.

def set_session(request):
    request.session['name']='Shubham Pandey'
    return render(request,'app/set_session.html')


def getsession(request):
    name = request.session['name']   # request.session.get('name')
    return render(request,'app/get_session.html',{'name':name})


def delsession(request):
    if 'name' in request.session:
        del request.session['name']    
    return render(request,'app/del_session.html')    
