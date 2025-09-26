from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User, Task

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Імʼя користувача'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Підтвердіть пароль'
        })

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        input_formats=['%d.%m.%Y'],
        widget=forms.DateInput(
            format='%d.%m.%Y',
            attrs={
                'class': 'form-control',
                'type': 'text',
                'placeholder': 'дд.мм.рррр'
            }
        ),
        required=False
    )

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'due_date']

