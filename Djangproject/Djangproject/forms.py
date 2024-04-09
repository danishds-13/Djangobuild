from django import forms 

class UserForm(forms.Form):
    num1=forms.forms.CharField(label="username")   #to ignore the required field use the attribute required and set it to false and to use a class we must include a widget
    num2=forms.forms.CharField(label="email" required=False)