from django.db import models



class Todo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100 )
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)


class Article(models.Model):
    username = models.CharField(max_length=100)
    article = models.CharField(max_length=100)





class Test(models.Model):
    test = models.CharField(max_length=100)




"""class Register(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100 )
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user = models.CharField(max_length=100)"""




class Register1(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100 )
    password = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    user = models.CharField(max_length=100)