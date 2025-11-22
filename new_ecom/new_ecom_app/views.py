from django.shortcuts import render ,redirect
from new_ecom_app.models import student
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from new_ecom_app.form import registerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def index(request):
    content={}
    content['data'] = student.objects.filter(is_delete='N')
    return render(request, 'index.html', content)


#create for user form data submit in database
def forms(request):
        if request.method == 'POST':
            name = request.POST['name']
            dob = request.POST['dob']
            address = request.POST['address']
            email = request.POST['email']
            phone = request.POST['phone']
            
            t1=student.objects.create(name=name,dob=dob,address=address,email=email,phone=phone)
            # print(t1)
            # return HttpResponse("Data submitted successfully")
            t1.save()
            # You can add code here to save the data to the database if needed
            return redirect('/index')  # Redirect to a success page or another view
        else:
            return render(request, 'index.html')
        
# Create delete view

def delete(request, id):
    student.objects.filter(id=id).update(is_delete='Y')

    return redirect('/index')

# create edit view
# def edit(request, id):
#      if request.method == 'POST':
#             name = request.POST['name']
#             dob = request.POST['dob']
#             address = request.POST['address']
#             email = request.POST['email']
#             phone = request.POST['phone']
#             student.objects.filter(id=id).update(name=name,dob=dob,address=address,email=email,phone=phone)
#      else:
#         content = {}
#         content['data'] = student.objects.filter(id=id)
#         return render(request, 'index.html', content)


# create edit view

def edit(request, id):
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        address = request.POST['address']
        email = request.POST['email']
        phone = request.POST['phone']

        student.objects.filter(id=id).update(
            name=name, dob=dob,
            address=address, email=email,
            phone=phone
        )
        return redirect('/index')

    else:
        obj = student.objects.get(id=id)
        content = {'obj': obj, 'data': student.objects.filter(is_delete='N')}
        return render(request, 'index.html', content)

def give_group_permission(user):
    group1 = Group.objects.get(name="basic")
    group2 = Group.objects.get(name="hr")
    user.groups.add(group1, group2)
    user.save()

# def register(request):
    
#     if request.method=='POST':
#         username = request.POST['username']
#         password1 = request.POST['password1']
#         # print(username)
#         # print(password1)
#         user = User(username=username, password=password1, is_active=True, is_staff=True)
#         user.save()
#         give_group_permission(user)
#         return redirect('/register/')
#         # return redirect('/resgister')


#     else:
#         fm=UserCreationForm()
#         return render(request, 'signup.html', {'form':fm})

def register(request):
    if request.method == 'POST':
        fm=registerForm(request.POST)
        # print(fm)
        if fm.is_valid():
            messages.success(request, 'Account created successfully!, please login.')
            fm.save()
            
        return redirect('/register/')
    else:
        fm=registerForm()
        return render(request, 'signup.html', {'form':fm})

def header(request):
    return render(request, 'header.html')


def user_login(request):
    if request.method == 'POST':
        fm=AuthenticationForm(request=request, data=request.POST)
        # print(fm)
        # print(fm.is_valid())
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            # print(uname, upass)
            u=authenticate(username=uname, password=upass)
            # print(u)
            if u:
                login(request, u)
                return redirect('/index')
        # return HttpResponse("in post section")
    else:
        fm=AuthenticationForm()
        return render(request, 'login.html', {'form':fm})

def user_logout(request):
    logout(request)
    return redirect('/login')

def setcookie(request):
    r=render(request,'setcookie.html')
    r.set_cookie('name','new_ecom_cookie')
    # r.set_cookie('name','new_ecom_cookie',max_age=60)
    return r

def getcookie(request):
    # d=request.COOKIES['name']
    d=request.COOKIES.get('name','Hello Guest')
    return render(request,'getcookie.html',{'data':d})


def setsession(request):
    request.session['name']='new_ecom_session'
    return render(request,'setsession.html')

def getsession(request):
    d=request.session['name']
    return render(request,'getsession.html',{'data':d})

def del_session(request):
    if 'name' in request.session:
        del request.session['name']
    return HttpResponse("session deleted")


def getloggeduserid(request):
    user_id=request.user.id
    return render(request,'getloggeduserid.html',{'data':user_id})
