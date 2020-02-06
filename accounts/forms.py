from django import forms
from django.contrib.auth import (
    authenticate,
    get_user_model

)

User = get_user_model


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput)

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exists')
            if not user.check_password(password):
                raise froms.ValidationError('Incorrect Password')
            if not user.is_active:
                raise froms.ValidationError('This user is not active')
        return super(UserLoginForm, self).clean(*args, **kwargs)


class UserRegistrationForm(forms.ModelForm):
    number = forms.CharField(label='Mobile Number')
    number2 = forms.CharField(label='Confirm Mobile Number')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = user
        fields =[
            'username'
            'number'
            'number2'
            'password'
         ]

    def clean_number(self):
        number = self.cleaned_data.get('number')
        number2 = self.cleaned_data.get('number2')
        if number != number2:
            raise forms.ValidationError("Mobile Numbers must match")
        number_qs = User.objects.filter{number=number}
        if number_qs.exists():
            raise forms.ValidationError(
                "This number is already being used"
            )
        return number

