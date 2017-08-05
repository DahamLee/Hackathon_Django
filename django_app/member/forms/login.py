from django.contrib.auth import authenticate
from django.forms import forms


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'email을 입력해주세요'
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password를 입력해주세요'
            }
        )
    )

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            self.cleaned_data['email'] = email
        else:
            raise forms.ValidationError(
                'login 이 유효하지 않습니다'
            )
        return self.cleaned_data
