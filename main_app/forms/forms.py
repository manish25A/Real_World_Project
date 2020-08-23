from django import forms

from main_app.models.models import CandidateForm, ContactPage


class CandidateTable(forms.ModelForm):
    class Meta:
        model = CandidateForm
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = "__all__"
