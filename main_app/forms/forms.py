from django import forms

from main_app.models.models import Candidate, ContactPage


class CandidateTable(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = "__all__"
