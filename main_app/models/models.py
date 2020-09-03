from django.contrib.auth.models import User
from django.db import models


class Seeker(models.Model):
    seeker = models.ForeignKey(User, on_delete=models.CASCADE())
    seekerusername = models.CharField(max_length=50, unique=True)
    seekeremail = models.CharField(max_length=50, unique=True)
    seekerpassword = models.CharField(max_length=50)

    class Meta:
        pass


class seekerapply(models.Model):
    user_id = models.ForeignKey(Seeker, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phoneno = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    location = models.CharField(max_length=50)


class Provider(models.Model):
    name = models.CharField(max_length=50, unique=True)
    compname = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50)
    fyear = models.DateField(max_length=50)
    phoneno = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class jobpostmodel(models.Model):
    provider_id = models.ForeignKey(Provider, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50, default="name")
    lname = models.CharField(max_length=50)
    phno = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    compname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    jtitle = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=50)


class ContactPage(models.Model):
    contactname = models.CharField(max_length=50)
    contactemail = models.EmailField(unique=True)
    contactphoneno = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=500)
