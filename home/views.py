from urllib import request
from django.shortcuts import render , redirect
from .models import Todo , Article , Register1
from .forms import register
from .forms import TodoUpdateForm
from django.contrib.auth.models import User
from visitor.views import admin_login


def homepage(request):
    all=User.objects.all()
    return render(request,'home.html',{'todo':all})

def managepage(request):
    all=User.objects.all()
    return render(request,'manage.html',{'Todo':all})



def registerpage(request):


    if request.method=='POST':
        first = request.POST['first_name']
        last = request.POST['last_name']
        usern = request.POST['username']
        pas = request.POST['password']
        coun=request.POST['country']
        prou=request.POST['province']
        city=request.POST['city']
        user=request.POST['user']

        Register1.objects.create(first_name=first,
                               last_name=last,
                               username=usern,
                               password=pas,
                               country=coun,
                               province=prou,
                               city=city,
                               user=user)
        return render(request,'home.html')



    return render(request,'register.html')
 
"""  
def articles(request):
    all=Article.objects.all()
    all2=User.objects.all()

    return render(request,'articles.html',{'articles':all,
                                           'Todo':all2})"""

"""def article(request):
    if request.method == 'POST':
        user=request.POST['username']
        art=request.POST['article']
        print(user)
        Article.objects.create(username=user,
                               article=art)
    all = User.objects.all()
    return render (request,'addarticle.html', {'todo':all})
    
def details(request, Register1_id):
	todo = User.objects.get(id=Register1_id)
	return render(request, 'detail.html', {'todo':todo})"""

def delete(request, Register1_id):
	User.objects.get(id=Register1_id).delete()
	return render(request,'home.html')

def update(request, Register1_id):
	User.objects.get(id=Register1_id).delete()
	return render(request,'update.html')


def loginpage(request):
    return render (request,'loginuser.html')

def start(request):
    return render (request,'start.html')

    return redirect (start)
    
"""def LoginPage(request):
    def a(request)    :
        todo=Register1.objects.get(user=todo_use)
        if todo == "admin":
            def HomePageAdmin(request):
                pass
        else:
            def HomePageUser(request):"""
                            






