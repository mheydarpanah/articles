from django.urls import path
from .views import homepage
import home.views
import visitor.views

urlpatterns = [
    path('', visitor.views.admin_login),
    path('register/', visitor.views.normalregister),
    path('home/' , visitor.views.home),
    path('homepage/', home.views.homepage),
    path('manage/', visitor.views.managepage),
    path('login/', home.views.loginpage),
    path('register/', home.views.registerpage),
    path('article/', visitor.views.article),
    path('articles/', visitor.views.articles),
    path('details/<int:User_id>/', visitor.views.details, name='details'),
    path('delete/<int:User_id>/', visitor.views.delete, name='delete'),
    path('update/<int:User_id>/', visitor.views.update, name='update'),




]