from djongo import models


class Seeker(models.Model):
    id = models.ObjectIdField()
    seekerusername = models.CharField(max_length=50, unique=True)
    seekeremail = models.CharField(max_length=50, unique=True)
    seekerpassword = models.CharField(max_length=50)
    objects = models.DjongoManager()


class seekerapply(models.Model):
    id = models.ObjectIdField()
    seekerusername = models.CharField(max_length=50, unique=True)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profession = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    objects = models.DjongoManager()


class Provider(models.Model):
    id = models.ObjectIdField()
    name = models.CharField(max_length=50, unique=True)
    compname = models.CharField(max_length=50, unique=True)
    email = models.CharField(max_length=50)
    fyear = models.DateField(max_length=50)
    phoneno = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    objects = models.DjongoManager()


class jobpostmodel(models.Model):
    id = models.ObjectIdField()
    fname = models.CharField(max_length=50, default="name")
    lname = models.CharField(max_length=50)
    phno = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    compname = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    jtitle = models.CharField(max_length=50)
    salary = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    objects = models.DjongoManager()


class ContactPage(models.Model):
    id = models.ObjectIdField()
    contactname = models.CharField(max_length=50)
    contactemail = models.EmailField(unique=True)
    contactphoneno = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=500)
    objects = models.DjongoManager()
