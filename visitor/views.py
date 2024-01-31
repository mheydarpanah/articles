from urllib import request
from django.shortcuts import render , redirect
from django.contrib import messages 
from .forms import UserLoginForm
from django.contrib.auth import authenticate, login, logout 
from home.models import  Register1 , Article
from home.forms import register
from django.contrib.auth.models import User



def start(request):
    return render (request,'test.html')

"""def normalregister(request):
    
    if request.method=='POST':
        first = request.POST['first_name']
        last = request.POST['last_name']
        usern = request.POST['username']
        pas = request.POST['password']


        form=register(request.POST)
        if form.is_valid():
           cd= form.cleaned_data
           User.objects.create(first_name=first,
                               last_name=last,
                               Username=usern,
                               Password=pas,
)
           return render(request,'visitorhome.html',{'data':cd})

    return render(request,'registertest.html')"""





def admin_login(request):
    if request.method=='POST':
        global first
        first = request.POST['username']
        last = request.POST['password']
        global userlogin
        userlogin = authenticate (request, username=first, password=last)
        if userlogin is not None:
            login(request, userlogin)
            messages.success(request, 'logged in successfully', 'success')
            global ff
            ff = userlogin
            return render(request ,'home.html' ,{'cd':ff})
        else:
            messages.error(request, 'username or password is wrong', 'danger')
            
    return render(request, 'test.html')

def home(request):
    if User is login:
        return render (request,'home.html')
    return redirect ('http://127.0.0.1:8000')


def normalregister(request):
    if request.method =='POST':
        f=request.POST['first_name']
        l=request.POST['last_name']
        u=request.POST['username']
        e=request.POST['email']
        p=request.POST['password']
        user = User.objects.create_user(u, e, p)
        user.first_name = f
        user.last_name = l
        user.save()


    return render (request,'registertest.html')




def article(request):
    if request.method == 'POST':
        user=request.POST['user']
        art=request.POST['article']
        print(user)
        Article.objects.create(username=user,
                               article=art)
    all = User.objects.all()
    
    return render (request,'addarticle.html', {'todo':all , 
                                               'cd':ff,
                                            'user':first})




def articles(request):
    all=Article.objects.all()
  

    return render(request,'articles.html',{'articles':all,
                                            'user':first})
                                           
                                           
                                           
def user_logout(request):
	hh=logout(request)
	messages.success(request, 'logged out successfully', 'success')

	return render(request,'home.html',{'ff':ff})

""" all2=User.objects.all()"""  



def details(request, User_id):
	todo = User.objects.get(id=User_id)
	return render(request, 'detail.html', {'todo':todo})






#-------------------------------home view--------------------------------









def homepage(request):
    all=User.objects.all()
    return render(request,'home.html',{'todo':all})

def managepage(request):
    all=User.objects.all()
    if first == "root":
        return render(request,'manage.html',{'Todo':all,
                                             'user':first})

    else:
        return render(request, 'grid.html',{'Todo':all,
                                            'user':first})

    return render(request,'manage.html',{'Todo':all},{'Todo':all,
                                                      'user':first})



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

def delete(request, User_id):
	User.objects.get(id=User_id).delete()
	return render(request,'home.html')

def update(request, User_id):
	User.objects.get(id=User_id).delete()
	return render(request,'update1.html')


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