from django.shortcuts import render
from django.http import HttpResponse
from urllib import request
from django.shortcuts import render , redirect
from home.models import Todo , Article , Register1


def homepage(request):
    all=Register1.objects.all()
    return render(request,'home.html',{'todo':all})

def managepage(request):
    all=Register1.objects.all()
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

        form=register(request.POST)
        if form.is_valid():
           cd= form.cleaned_data
           Register1.objects.create(first_name=first,
                               last_name=last,
                               username=user,
                               password=pas,
                               country=coun,
                               province=prou,
                               city=city,
                               user=user)
           return render(request,'home.html',{'data':cd})


    else:
        form=register()
    return render(request,'register.html',{'form':form})
 
  
def articles(request):
    all=Article.objects.all()
    all2=Register1.objects.all()

    return render(request,'articles.html',{'articles':all,
                                           'Todo':all2})

def article(request):
    if request.method == 'POST':
        user=request.POST['username']
        art=request.POST['article']
        print(user)
        Article.objects.create(username=user,
                               article=art)
    all = Register1.objects.all()
    return render (request,'article.html', {'todo':all})
    
def details(request, Register1_id):
	todo = Register1.objects.get(id=Register1_id)
	return render(request, 'detail.html', {'todo':todo})

def delete(request, Register1_id):
	Register1.objects.get(id=Register1_id).delete()
	return render(request,'home.html')

def update(request, Register1_id):
	Register1.objects.get(id=Register1_id).delete()
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
                            







def LoginPage(request):
    return render(request,'loginadmin.html')