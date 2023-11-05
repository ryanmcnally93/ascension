from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('category', 'sku', 'name', 'description',
            'main_image', 'image', 'image_2', 'image_3',
            'is_hire_room', 'striked_price', 'price')

    main_image = forms.ImageField(label='Main Image', required=False, widget=CustomClearableFileInput)
    image = forms.ImageField(label='Image 1', required=False, widget=CustomClearableFileInput)
    image_2 = forms.ImageField(label='Image 2', required=False, widget=CustomClearableFileInput)
    image_3 = forms.ImageField(label='Image 3', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
