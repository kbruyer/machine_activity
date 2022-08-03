from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class DailyReportForm(forms.Form):
    created = forms.DateTimeField()
    description = forms.CharField()
