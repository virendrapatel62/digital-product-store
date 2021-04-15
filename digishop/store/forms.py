from django import forms


class CheckoutForm(forms.Form):
    email = forms.EmailField(max_length=30)
    phone = forms.CharField(max_length=10)
