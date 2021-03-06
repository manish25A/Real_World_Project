from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm

from accounts.models import User


# creating form for  registering the employee using usercreationform class provided by django
class EmployeeRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        # creating fields and  labels and placeholders for creation fomr
        super(EmployeeRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "First Name"
        self.fields['last_name'].label = "Last Name"
        self.fields['address'].label = "Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Enter Your Address',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

        # meta class with models and fields with error messages

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'address', 'email', 'password1', 'password2']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            },
            'address': {
                'required': 'Address is required',
                'max_length': 'Address is too long'
            },

        }

        # save using manager and role

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "employee"
        if commit:
            user.save()
        return user


# creating form for  registering the employer using usercreationform class provided by django
class EmployerRegistrationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        # creating fields
        super(EmployerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].label = "Company Name"
        self.fields['last_name'].label = "Company Address"
        self.fields['password1'].label = "Password"
        self.fields['password2'].label = "Confirm Password"

        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Company Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Company Address',
            }
        )
        self.fields['email'].widget.attrs.update(
            {
                'placeholder': 'Enter Email',
            }
        )
        self.fields['password1'].widget.attrs.update(
            {
                'placeholder': 'Enter Password',
            }
        )
        self.fields['password2'].widget.attrs.update(
            {
                'placeholder': 'Confirm Password',
            }
        )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']
        error_messages = {
            'first_name': {
                'required': 'First name is required',
                'max_length': 'Name is too long'
            },
            'last_name': {
                'required': 'Last name is required',
                'max_length': 'Last Name is too long'
            }
        }
        # saving as employer

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.role = "employer"
        if commit:
            user.save()
        return user


# user login form
class UserLoginForm(forms.Form):
    #defining the form fields
    email = forms.EmailField()
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput,
    )

    #using default constructor class to keep placeholders
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.fields['email'].widget.attrs.update({'placeholder': 'Enter Email'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Enter Password'})

#getting the data  for authentication
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")

        if email and password:
            self.user = authenticate(email=email, password=password)

            if self.user is None:
                raise forms.ValidationError("User or Password does not match.")
            if not self.user.check_password(password):
                raise forms.ValidationError("Password Does not Match.")
            if not self.user.is_active:
                raise forms.ValidationError("User is not Active.")

        return super(UserLoginForm, self).clean()

    def get_user(self):
        return self.user

#update form for employee
class EmployeeProfileUpdateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EmployeeProfileUpdateForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {
                'placeholder': 'Enter First Name',
            }
        )
        self.fields['last_name'].widget.attrs.update(
            {
                'placeholder': 'Enter Last Name',
            }
        )
        self.fields['address'].widget.attrs.update(
            {
                'placeholder': 'Enter Address',
            }
        )

    class Meta:
        model = User
        fields = ["first_name", "last_name", "address"]
