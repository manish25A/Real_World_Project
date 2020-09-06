from django import forms

from main_app.models.models import Job, Applicant, ContactPage


# creating job form after connecting to model and checking if the form data is valid or not
class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ('user', 'created_at',)
        labels = {
            "last_date": "Last Date",
            "company_name": "Company Name",
            "company_description": "Company Description"
        }
        # checking the data validation of the form

    def is_valid(self):
        valid = super(CreateJobForm, self).is_valid()

        # if already valid, then return True
        if valid:
            return valid
        return valid

    # saving the data only if the data is saved in JobForm
    def save(self, commit=True):
        job = super(CreateJobForm, self).save(commit=False)
        if commit:
            job.save()
        return job


# getting the data from form  and saving it to model applicant
class ApplyJobForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ('job',)


# getting the data from jobform and saving it to model
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = "__all__"
