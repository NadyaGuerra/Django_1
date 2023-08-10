from django import forms

from catalog.models import Product
from catalog.models import Version
class ProductForm(forms.ModelForm):
        class Meta:
            model = Product
            fields = ('name', 'description', 'category', 'preview', 'price')

        def clean_name(self):
            cleaned_data = self.cleaned_data['name']

            if cleaned_data in (
                    'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'):
                raise forms.ValidationError('Запрещенное название товара')
            return cleaned_data

        def clean_description(self):
            cleaned_data = self.cleaned_data['description']

            if cleaned_data in (
                    'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'):
                raise forms.ValidationError('Запрещенное слово в описании товара')
            return cleaned_data

        def __int__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'