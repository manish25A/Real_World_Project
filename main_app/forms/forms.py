from django import forms

from main_app.models.models import Candidate, ContactPage, jobpostmodel


class CandidateTable(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = "__all__"


class jobpostform(forms.ModelForm):
    class Meta:
        model = jobpostmodel
        fields = "__all__"
