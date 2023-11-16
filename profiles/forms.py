from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = (
            "full_name",
            "default_street_address1",
            "default_street_address2",
            "default_town_or_city",
            "default_postcode",
            "default_phone_number",
        )

    # Here we are overriding the normal init method
    def __init__(self, *args, **kwargs):
        # This is the default init method
        super().__init__(*args, **kwargs)
        # Comment this out and look at the difference
        placeholders = {
            "full_name": "Full Name",
            "default_postcode": "Post Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_phone_number": "Phone Number",
        }

        # This is just setting the focus automatically to where we want it
        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        # This adds stars to the required fields
        # And sets revelant placeholder names to their inputs
        # Also adds a css class
        # And removes labels as we have placeholders
        # Comment out to see differences
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f"{placeholders[field]} *"
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "rounded-0"
            self.fields[field].label = False
        for field_name, field in self.fields.items():
            if field_name == "default_phone_number":
                field.widget.attrs["minlength"] = "11"
                field.widget.attrs["maxlength"] = "11"
                field.widget.attrs["pattern"] = "[0-9]+"
            else:
                field.widget.attrs["minlength"] = "4"
                field.widget.attrs["pattern"] = "[a-zA-Z0-9 ]+"
