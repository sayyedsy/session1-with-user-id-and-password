from django.shortcuts import render
from .models import login
from .forms import loginform

# Create your views here.
def login1(request):
    fm=loginform()
    return render(request,'login.html',{'form':fm})


def success(request):
    user=request.POST['username']
    password=request.POST['password']
    use=login.objects.get(username=user)
    if use.password==password:
        request.session['username']=user
        return render(request,'success.html',{'use':use})
    else:
        fm = loginform()
        return render(request, 'login.html', {'form': fm})


def save123(request):
    li=request.POST.getlist('items')
    #request.session['item']=li
    user=request.session['username']
    item1=request.session['item']
    return render(request,'save.html',{'user':user,'item1':li})