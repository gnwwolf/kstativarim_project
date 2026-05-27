from django import forms
from django.core.validators import RegexValidator
from .models import Order, ContactRequest


class OrderForm(forms.ModelForm):
    """Форма для заказа услуги"""
    name = forms.CharField(
        label='Ваше имя',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Иван Иванов'
        })
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?7[\s\-]?\(?[0-9]{3}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                message='Введите номер в формате: +7 (XXX) XXX-XX-XX'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+7 (987) 379-00-39'
        })
    )
    custom_request = forms.CharField(
        label='Пожелания (необязательно)',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Опишите, что нужно сделать...'
        })
    )
    class Meta:
        model = Order
        fields = ['name', 'phone', 'service', 'custom_request']
        widgets = {
            'service': forms.Select(attrs={'class': 'form-select'})
        }


class ContactForm(forms.ModelForm):
    """Форма для заявки на консультацию"""

    name = forms.CharField(
        label='Ваше имя',
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Иван Иванов'
        })
    )
    phone = forms.CharField(
        label='Телефон',
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?7[\s\-]?\(?[0-9]{3}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$',
                message='Введите номер в формате: +7 (XXX) XXX-XX-XX'
            )
        ],
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+7 (987) 379-00-39'
        })
    )
    message = forms.CharField(
        label='Сообщение (необязательно)',
        required=False,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Ваш вопрос...'
        })
    )
    class Meta:
        model = ContactRequest
        fields = ['name', 'phone', 'message']