from django import forms
from app.models import ShippingAddress
class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['address','city','state','mobile','email',]
        # Tao Css cho Dep
        widgets = {'address': forms.TextInput(attrs={'class': 'form-control'}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'state': forms.TextInput(attrs={'class': 'form-control'}),
                   'mobile': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
