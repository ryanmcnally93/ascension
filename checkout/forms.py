from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone_number',
                  'street_address1', 'street_address2',
                  'town_or_city', 'postcode',)

    # Here we are overriding the normal init method
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        # This is the default init method
        super().__init__(*args, **kwargs)
        # Comment this out and look at the difference
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email Address',
            'phone_number': 'Phone Number',
            'postcode': 'Post Code',
            'town_or_city': 'Town or City',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
        }

        # This is just setting the focus automatically to where we want it
        self.fields['full_name'].widget.attrs['autofocus'] = True
        # This adds stars to the required fields
        # And sets revelant placeholder names to their inputs
        # Also adds a css class
        # And removes labels as we have placeholders
        # Comment out to see differences
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
            self.fields['phone_number'].widget.attrs['type'] = 'number'
        for field_name, field in self.fields.items():
            if field_name == 'phone_number':
                field.widget.attrs['minlength'] = '11'
                field.widget.attrs['maxlength'] = '11'
                field.widget.attrs['pattern'] = '[0-9]+'
            elif field_name != 'email':
                field.widget.attrs['pattern'] = '[a-zA-Z0-9 ]+'
                field.widget.attrs['minlength'] = '4'
