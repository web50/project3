from django import forms
from .models import Topping
from django.contrib.auth.models import User

class RegisterForm(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True,widget=forms.TextInput())

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

class LoginForm(forms.Form):


    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class ToppingsForm(forms.ModelForm):

    all_toppings = [(topping.description) for topping in Topping.objects.all()]

    toppings = forms.MultipleChoiceField(choices=all_toppings, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Topping
        fields = ['description']