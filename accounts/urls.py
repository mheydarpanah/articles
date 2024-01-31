from django.urls import path
from accounts.views import LoginPage
import accounts.views

urlpatterns = [
    path('login/', accounts.views.LoginPage),


]