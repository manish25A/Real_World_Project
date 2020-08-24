from djongo import models


class Candidate(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=20)
    category = models.CharField(max_length=50)

    class Meta:
        db_table = 'candidate'


class CandidateApply(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profession = models.CharField(max_length=50)
    Location = models.CharField(max_length=50)
    curstats = models.CharField(max_length=50)
    img = models.ImageField(max_length=50, default='img.jpg')


class ContactPage(models.Model):
    name = models.CharField(max_length=50, default="name")
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, default="phone")
    message = models.TextField(max_length=500, default="Message")

    class Meta:
        db_table = 'contactpage'
