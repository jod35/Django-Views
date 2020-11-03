from django import forms


class MyForm(forms.Form):
    username=forms.CharField(max_length=200)
    email=forms.CharField(widget=forms.EmailInput(attrs={'placeholder':"Enter yo mama"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Enter a password Nigga"}))
    confirm=forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':"Should equal to what you entered"}))

    