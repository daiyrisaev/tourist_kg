from django import forms
from django.contrib.auth.models import User
# Есть 2 вида форм
# ModelForm - формы основанные на полях модели
# Form - Обычная форма


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        widgets = {'user_name': forms.TextInput(attrs={'class': 'floatlabel','placeholder':'имя пользователя'}),'password':forms.PasswordInput(attrs={"class":"floatlabel"})}


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='password',widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','first_name','email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return cd['password2']