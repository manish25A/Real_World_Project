from djongo import models


class CandidateForm(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)
    company_name = models.CharField(max_length=150)
    phone_no = models.CharField(max_length=20)
    category = models.CharField(max_length=50)

    class Meta:
        db_table = 'candidate'
