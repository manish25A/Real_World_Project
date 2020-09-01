from django import forms

from main_app.models.models import Seeker, ContactPage, jobpostmodel, seekerapply, Provider


class seekerform(forms.ModelForm):
    class Meta:
        model = Seeker
        fields = "__all__"


class providerform(forms.ModelForm):
    class Meta:
        model = Provider
        fields = "__all__"


class contactform(forms.ModelForm):
    class Meta:
        model = ContactPage
        fields = "__all__"


class jobpostform(forms.ModelForm):
    class Meta:
        model = jobpostmodel
        fields = "__all__"


class seekerapplyform(forms.ModelForm):
    class Meta:
        model = seekerapply
        fields = "__all__"
