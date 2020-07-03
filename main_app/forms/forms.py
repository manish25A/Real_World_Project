from django import forms

from main_app.models.models import CandidateForm, ContactPage, CustomerEmail


class CandidateForm(forms.ModelForm):
    class Meta:
        model = CandidateForm
        fields = "__all__"


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = "__all__"


class CustomerEmailForm(forms.ModelForm):
    class Meta:
        model = CustomerEmail
        fields = "__all__"
