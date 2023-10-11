
from django import forms

from cart.models import Order

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)


class OrderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(OrderForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs = {
            'placeholder': 'Enter your first name',
            'class': 'form-control',
            'required': True
        }
        self.fields['last_name'].widget.attrs = {
            'placeholder': 'Enter your last name',
            'class': 'form-control',
            'required': True
        }
        self.fields['email'].widget.attrs = {
            'placeholder': 'Enter your mail',
            'class': 'form-control',
            'required': True
        }
        self.fields['address'].widget.attrs = {
            'placeholder': 'Enter your destination adress',
            'class': 'form-control',
            'required': True
        }

        self.fields['number'].widget.attrs = {
            'placeholder': 'Enter your phone number',
            'class': 'form-control',
            'required': False
        }
        self.fields['date'].widget.attrs = {
            'placeholder': 'Choose delivery date',
            'class': 'form-control',
            'required': False
        }

        self.fields['comments'].widget.attrs = {
            'placeholder': 'Any comments?',
            'class': 'form-control',
            'required': False
        }

    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email', 'address', 'number',
                  'date', 'comments', )
        widgets = {
            'date': forms.DateInput(format=('%m/%d/%Y'),
                                    attrs={'class': 'form-control', 'placeholder': 'date delivery','type': 'date'}),
        }
