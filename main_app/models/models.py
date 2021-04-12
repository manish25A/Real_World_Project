from django.db import models
from django.utils import timezone

from accounts.models import User

# creating job model
JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    location1 = models.CharField(max_length=150)
    type = models.CharField(choices=JOB_TYPE, max_length=10)
    last_date = models.DateTimeField()
    company_name = models.CharField(max_length=100)
    company_description = models.CharField(max_length=300)
    created_at = models.DateTimeField(default=timezone.now)
    filled = models.BooleanField(default=False)
    salary = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.title


# creating applicant model
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applicants')
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ['user', 'job']

    def __str__(self):
        return self.user.get_full_name()


# creating contactpage model
class ContactPage(models.Model):
    id = models.AutoField(primary_key=True)
    contactname = models.CharField(max_length=50)
    contactemail = models.EmailField(unique=True)
    contactphoneno = models.CharField(max_length=20)
    subject = models.CharField(max_length=20)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.contactname
