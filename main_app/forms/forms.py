from django import forms

from main_app.models.models import CandidateForm


class CandidateSign(forms.ModelForm):
    class Meta:
        model = CandidateForm
        fields = "__all__"
