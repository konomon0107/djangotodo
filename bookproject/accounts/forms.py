from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import CustomUser  # Import the CustomUser model from your app
from bookproject.backends import CustomAuthenticationBackend

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='必須項目です。有効なメールアドレスを入力してください。')

    class Meta:
        model = CustomUser  # Use CustomUser instead of User
        fields = ('username', 'email', 'password1', 'password2')

class CustomAuthenticationForm(forms.Form):
    email = forms.CharField(max_length=254, help_text='必須項目です。有効なメールアドレスを入力してください。')
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = CustomAuthenticationBackend().authenticate(request=None, username=email, password=password)
        if user is None:
            raise forms.ValidationError('メールアドレスまたはパスワードが正しくありません。')
