from django.contrib.auth import get_user_model
from django.forms import forms

User = get_user_model()


class SignupForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Email 은 중복이 불가능합니다'
            }
        )
    )

    nickname = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Nickname은 중복 가능합니다'
            }
        )
    )

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password를 입력해주세요'
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'password를 다시 입력해주세요'
            }
        )
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email and User.objects.filter(username=email).exists():
            raise forms.ValidationError(
                '이미 존재하는 email 입니다'
            )
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'password가 동일하지 않습니다'
            )
        return password2

    def create_user(self):
        email = self.cleaned_data['email']
        password = self.cleaned_data['password2']
        nickname = self.cleaned_data['nickname']

        user = User.objects.create_user(
            email=email,
            password=password,
            nickname=nickname,
        )
        return user
